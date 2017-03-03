request = require('request')

module.exports = function (context, myBlob) {
    
    context.log("JavaScript blob trigger function processed blob \n Name:", context.bindingData.name, "\n Blob Size:", myBlob.length, "Bytes");
    
    var baseUrl = process.env.BLOB_STORAGE_URL;
    var url = baseUrl + context.bindingData.name;
    context.log(url);

    requestBody = JSON.stringify({"url":url})

    // ping API
    request.post({
        headers: {'content-type' : 'application/json', 'Ocp-Apim-Subscription-Key' : process.env.API_KEY},
        url: 'https://westus.api.cognitive.microsoft.com/vision/v1.0/tag',
        body: requestBody,
    }, function(error, response, body){
        if(error) {
            context.log(error);
        } else {
            var results = JSON.parse(body).tags;
            var tags = [];
            for (var i = 0; i < results.length; i++) {
                var result = results[i];
                var tag = result.name;
                var confidence = result.confidence;
                if (confidence > 0.7) {
                    tags.push(tag);
                }
            }
            context.log(tags);
            
            context.bindings.outputTable = {
                "partitionKey": "image-metadata",
                "rowKey": context.bindingData.name,
                "Tags": tags
            }

            context.done();
        }
    });
};