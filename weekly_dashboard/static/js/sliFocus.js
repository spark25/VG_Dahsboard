
//GLOBAL CONFIGURATIONS
Chart.defaults.global.tooltips.mode ='index',
Chart.defaults.global.tooltips.intersect =false,
Chart.defaults.global.tooltips.titleFontSize = 14;
Chart.defaults.global.tooltips.bodyFontSize = 12;
Chart.defaults.global.tooltips.bodySpacing = 4;
Chart.defaults.global.elements.point.radius =5;
Chart.defaults.global.elements.point.hoverRadius = 10;
Chart.defaults.global.elements.line.borderWidth = 1;
Chart.defaults.global.elements.line.tension = 0 ;
// Chart.defaults.scale.gridLines.display  =false;

//GLOBAL CONFIGURATIONS above

function create_reg_focus(){
    let reg_focus_x_axis = []
    let reg_y_focus_axis = []
{% for x  in reg_data %}
    reg_focus_x_axis.push('{{ x.date_time }}') 
    reg_y_focus_axis.push(parseInt('{{ x.count }}'))
{% endfor%}
const reg_chart_focus = document.getElementById('reg_chart_focus').getContext('2d');
var chart = new Chart(reg_chart_focus, {

    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: reg_focus_x_axis,
        datasets: [{
            // lineTension: 0,
            // fill: false,
            label: "Registrations",
            borderColor: 'rgba(34, 167, 240, 1)',
            backgroundColor:'rgba(34, 167, 240, 0.1)',
            data: reg_y_focus_axis,
            // pointRadius:5,
            // pointHoverRadius:10,
        }]
    },

    // Configuration options go here
    options: {
    scales: {
        xAxes: [{
            ticks: {
                callback: function(value, index, values) {
                    return value.substring(0, 7);
                }
            }
        }]
    }
}
});
}


