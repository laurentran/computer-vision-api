request = require('request')

module.exports = function (context, myBlob) {
    
    context.log("JavaScript blob trigger function processed blob \n Name:", context.bindingData.name, "\n Blob Size:", myBlob.length, "Bytes");
    
    var baseUrl = process.env.BLOB_STORAGE_URL;
    var url = baseUrl + context.bindingData.name + '/' + context.bindingData.slice;
    context.log(url);

    requestBody = JSON.stringify({"url":url})

    //ping API
    request.post({
        headers: {'content-type' : 'application/json', 'Prediction-Key' : process.env.IRIS_KEY},
        url: process.env.IRIS_URL,
        body: requestBody,
    }, function(error, response, body){
        if(error) {
            context.log(error);
        } else {
            var results = JSON.parse(body);
            results = results.Classifications;
            var result = results[0];
            var tag = result.Class;
            var confidence = result.Probability;
            if (confidence > 0.5) {
                context.log(tag);
            }
            
            //write to table
            context.bindings.outputTable = {
                "partitionKey": context.bindingData.name,
                "rowKey": context.bindingData.slice,
                "Logo": tag
            }

            context.done();
        }
    });
};