function buildBubble() {
  d3.json("/api/similarity_scores").then((data, err) => {
    if (err) throw err;
    console.log(data);

    //Get first 15 records
    const slicedArray = data.slice(0, 15);
    console.log(slicedArray);

    // Get data needed from json
    var budget = slicedArray.map(d => d.budget);
    var revenue = slicedArray.map(d => d.revenue);
    var similarity = [];
    for (var i=0; i<slicedArray.length; i++) {
      var random = Math.random();
      similarity.push(random);
    }
    console.log(similarity);
    var title = slicedArray.map(d => d.title);
    var genres = slicedArray.map(d => d.genres);
    var director = slicedArray.map(d => d.director);
    var release = slicedArray.map(d=> d.release_date)
    var runtime = slicedArray.map(d=> d.runtime)
    var Hoverinfo = []
    for (i=0;i<director.length;i++){
      p = {"Title":title[i], "Genre": genres[i], "Director":director[i],
          "Release_Date":release[i],"Run_Time":runtime[i]+" min."}
      Hoverinfo.push(p)
    }
    // Build BUBBLE
    var data = [{
      x: revenue,
      y: budget,
      text: Hoverinfo,
      mode: 'markers',
      marker: {
        size: similarity * 100000000,
        color: revenue,
        //colorscale: "RdBu"
      },
      hovertemplate:
      "<b>Title:</b> %{text.Title}<br><b>Genre:</b> %{text.Genre}<br><b>Director:</b> %{text.Director}<br><b>Release Date:</b> %{text.Release_Date} <br> <b>Run Time:</b>%{text.Run_Time}<extra></extra>"
    }];
    var layout = {
      title: `Female Lead or Directed Film Recommendations`,
      font: { size: 13 },
      xaxis: { title: "Revenue" },
      yaxis: {title: "Budget"}
    };
    Plotly.newPlot('bubble', data, layout); 
  });  //close json
}
// -------------------------------------------------- //
// Build Table
//Get a reference to the table body
var tbody = d3.select("tbody");

function buildTable() {
  d3.json("/api/similarity_scores").then((data, err) => {
    if (err) throw err;
    console.log(data);

    //Get first 15 records
    const slicedArray = data.slice(0, 15);
    console.log(slicedArray);

    var newData = [];
    slicedArray.forEach(obj => { 
    newData.push({"title": obj.title, "genres": obj.genres, "director": obj.director, "cast": obj.cast, "release_date": obj.release_date, 
                  "runtime": obj.runtime, "budget": obj.budget, "revenue": obj.revenue});  
    });
    console.log(newData);

    newData.forEach(obj => {
      var row = tbody.append("tr");
      Object.entries(obj).forEach(([key, value]) => row.append("td").text(value));
    });  
  });
}   
//------------------------------------------------------------
buildBubble();
buildTable();