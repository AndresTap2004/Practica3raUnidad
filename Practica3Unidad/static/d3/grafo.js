var nodes = new vis.DataSet([{id: 1,label:"1"},
{id: 2,label:"2"},
{id: 3,label:"3"},
{id: 4,label:"4"},
{id: 5,label:"5"},
{id: 6,label:"6"},
{id: 7,label:"7"},
{id: 8,label:"8"},
{id: 9,label:"9"},
{id: 10,label:"10"},
]);
var edges = new vis.DataSet([{from:1,to:4, label:"0.7179"},
{from:1,to:5, label:"0.0927"},
{from:1,to:9, label:"1261.4231"},
{from:1,to:10, label:"1267.0996"},
{from:2,to:3, label:"1.3757"},
{from:2,to:4, label:"1.7816"},
{from:2,to:5, label:"1.1502"},
{from:2,to:7, label:"1261.4683"},
{from:3,to:2, label:"1.3757"},
{from:3,to:6, label:"1263.663"},
{from:4,to:1, label:"0.7179"},
{from:4,to:2, label:"1.7816"},
{from:4,to:8, label:"1267.2946"},
{from:5,to:1, label:"0.0927"},
{from:5,to:2, label:"1.1502"},
{from:5,to:7, label:"1262.3693"},
{from:5,to:8, label:"1266.5321"},
{from:6,to:3, label:"1263.663"},
{from:6,to:8, label:"4.1916"},
{from:6,to:9, label:"3.8796"},
{from:7,to:2, label:"1261.4683"},
{from:7,to:5, label:"1262.3693"},
{from:7,to:8, label:"5.6876"},
{from:7,to:10, label:"7.3858"},
{from:8,to:4, label:"1267.2946"},
{from:8,to:5, label:"1266.5321"},
{from:8,to:6, label:"4.1916"},
{from:8,to:7, label:"5.6876"},
{from:8,to:9, label:"5.2345"},
{from:9,to:1, label:"1261.4231"},
{from:9,to:6, label:"3.8796"},
{from:9,to:8, label:"5.2345"},
{from:9,to:10, label:"11.8626"},
{from:10,to:1, label:"1267.0996"},
{from:10,to:7, label:"7.3858"},
{from:10,to:9, label:"11.8626"},
]);
var container = document.getElementById('mynetwork'); var data = {nodes: nodes, edges: edges}; var options = {}; var network = new vis.Network(container, data, options);