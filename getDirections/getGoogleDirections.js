var fs = require("fs");
 var content = fs.readFileSync("directions.json");

function getStrings(obj) {
  var data = JSON.parse(obj);
  var i = 0;
  var s = 0;
  console.log("Here are the starting points\n");
  for (i; i < data.routes[0].legs.length; i++) {
    console.log("Starting address : " + data.routes[0].legs[i].start_address);
    console.log("Ending address : " + data.routes[0].legs[i].end_address);
    console.log("Distance: " + data.routes[0].legs[i].distance.text);
    console.log("Time: " + data.routes[0].legs[i].duration.text);
    for (s; s < data.routes[0].legs[i].steps.length; s++) {
      if (data.routes[0].legs[i].hasOwnProperty("steps"))
      console.log(
        "Step " +
          s +
          ": " +
          data.routes[0].legs[i].steps[s].distance.text +
          "\r\n" +
          "Duration: " +
          data.routes[0].legs[i].steps[s].duration.text +
          "\r\n"
      );
      // console.log("Howdy");
      else{
      console.log("No steps found");
      }
    }
    console.log("\r\n");
  }
}

getStrings(content);
