// Load the Visualization API and the corechart package.
google.charts.load('current', {packages: ['corechart', 'line','bar']});
google.charts.setOnLoadCallback(regChart);
google.charts.setOnLoadCallback(canChart);
google.charts.setOnLoadCallback(assessChart);
google.charts.setOnLoadCallback(dailyAssessChart);
// Callback that creates and populates a data table,

//REGISTRATION
function regChart() {
  var graph_data = []
    {% for x  in reg_data %}
          graph_data.push(['{{x.date_time}}', parseInt('{{x.count}}')]) 
    {% endfor%}
  
  // Create the data table.
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'X');
  data.addColumn('number', 'count');
  data.addRows(graph_data);

  // Set chart options
  var options = {
  hAxis: {
    title: 'Date'
  },
  vAxis: {
    title: 'Count'
  },
  title:'Membership Registration By Date',
  width:500,
  height:350,
  colors:['#1abc9c']

};

  // Instantiate and draw our chart, passing in some options.
  var chart = new google.visualization.LineChart(document.getElementById('reg_chart_div'));
  chart.draw(data, options);
}



//CANCELLATION
function canChart() {
  var graph_data = []
    {% for x  in can_data %}
          graph_data.push(['{{x.date_time}}', parseInt('{{x.count}}')]) 
    {% endfor%}

  // Create the data table.
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'X');
  data.addColumn('number', 'count');
  data.addRows(graph_data);

  // Set chart options
  var options = {
  hAxis: {
    title: 'Date'
  },
  vAxis: {
    title: 'Count'
  },
  title:'Membership Cancellation By Date',
  width:500,
  height:350,
  colors:['#1abc9c']

};

  // Instantiate and draw our chart, passing in some options.
  var chart = new google.visualization.LineChart(document.getElementById('can_chart_div'));
  chart.draw(data, options);
}



//ASSESSMENT
  function assessChart() {

var data = new google.visualization.DataTable();

var graph_data = []
    {% for x  in assess_data %}
          graph_data.push(['{{x.event_type}}', parseInt('{{x.count__sum}}')]) 
    {% endfor%}

data.addColumn('string', 'Assessment');
data.addColumn('number', 'Assessment Processed');

data.addRows(graph_data);

var options = {
  title: 'Overview Of Assessment Processed',
  hAxis: {
    title: 'Assessment Type',
  },
  width:750,
  height:400 ,
  colors:['#1abc9c']
};

var chart = new google.visualization.ColumnChart(
  document.getElementById('assess_chart_div'));

chart.draw(data, options);
}


  // DAILY ASSESSMENT

  function dailyAssessChart() {
  // Some raw data (not necessarily accurate)
  var data = google.visualization.arrayToDataTable([
    ['Month', 'Bolivia', 'Ecuador', 'Madagascar', 'Papua New Guinea', 'Rwanda' ],
    ['2004/05',  165,      938,         522,             998,           450],
    ['2005/06',  135,      1120,        599,             1268,          288],
    ['2006/07',  157,      1167,        587,             807,           397],
    ['2007/08',  139,      1110,        615,             968,           215],
    ['2008/09',  136,      691,         629,             1026,          366]
  ]);

  var graph_data = []
  {% for x  in daily_assess %}
          graph_data.push(['{{x.event_type}}', '{{ x.date_time}}' ,parseInt('{{x.count}}')]) 
    {% endfor%}

  console.log(graph_data)

  var options = {
    title : 'Monthly Coffee Production by Country',
    vAxis: {title: 'Cups'},
    hAxis: {title: 'Month'},
    seriesType: 'bars',
  };

  var chart = new google.visualization.ComboChart(document.getElementById('daily_assess_chart_div'));
  chart.draw(data, options);
}