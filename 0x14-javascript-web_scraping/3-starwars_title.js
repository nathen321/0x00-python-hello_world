const request = require('request');
let url = "https://swapi-api.alx-tools.com/api/films/:id";
url = url.replace(":id" , process.argv[2]);
request(url, function (error, response, body) {
  console.log(JSON.parse(body).title);
});
