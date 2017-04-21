var fill = d3.scale.category20();
 /* var jsonTest = {
  "assigned infrastructure": 11, 
  "c software": 4, 
  "engineer ii": 5, 
  "foster farms": 5, 
  "infrastructure functions": 11, 
  "must able": 8, 
  "operating systems": 4, 
  "se ii": 7, 
  "within assigned": 7, 
  "years experience": 7
};*/


var ourData;
document.getElementById("button").addEventListener("click", function() {
  alert("WordCloud processing may take a long time depending on your file size");
  var ourRequest = new XMLHttpRequest();
  var e = '?n=' + document.getElementById("selector").value + '&word=' + document.getElementById("word").value;
  ourRequest.open('GET', 'http://127.0.0.1:5000/GetNgrams' + e);
  ourRequest.send();
  ourRequest.onload = function() {
    if (ourRequest.status >= 200 && ourRequest.status < 400) {
      ourData = JSON.parse(ourRequest.responseText);
      document.getElementById("wordCloud").innerHTML = "";
      DrawWordCloud();
      } else {
      console.log("We connected to the server, but it has returned an error.");
    }
  }})


    
   function DrawWordCloud(){
      var data = Object.values(ourData).map(function(d){ //change to Object.keys when using server
        //console.log(d);
        //console.log(jsonTest[d]);
        //console.log({text: d, size: 10 + ourData[index].value * 90});
        //return {text: d, size: 20 + ourData[d]}; Use this line when using server
        return {text: d, size: 30}; //Use this line when using serverV2 
      })


      d3.layout.cloud().size([800, 600])
          .words(data)
          .padding(5)
          .rotate(function() { return ~~(Math.random() * 2) * 90; })
          .font("Impact")
          .fontSize(function(d) { return d.size; })
          .on("end", draw)
          .start();

        function draw(words) {
          d3.select("#wordCloud").append("svg")
              .attr("width", 800)
              .attr("height", 600)
            .append("g")
              .attr("transform", "translate(400,300)")
            .selectAll("text")
              .data(words)
            .enter().append("text")
              .style("font-size", function(d) { return d.size + "px"; })
              .style("font-family", "Impact")
              .style("fill", function(d, i) { return fill(i); })
              .attr("text-anchor", "middle")
              .attr("transform", function(d) {
                return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
              })
              .text(function(d) { return d.text; });
            }


 } 




  