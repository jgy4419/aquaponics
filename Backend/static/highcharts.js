var chart;

function requestData() {
    $.ajax({
        url: '/chart',
        success: function(point) {
            var series = chart.series[0],
                shift = series.data.length > 20;
            chart.series[0].addPoint(point, true, shift);
        },
        cache: false
    });
}


$(document).ready(function() {

    humidity = new Highcharts.Chart({
        chart: chart[0],
        series: series[0],
        title: title[0],
        xAxis: xA[0],
        yAxis: yA[0]
        
    });
    temperature = new Highcharts.Chart({
        chart: chart[1],
        series: series[1],
        title: title[1],
        xAxis: xA[1],
        yAxis: yA[1]
        
    });
    soilHumidity = new Highcharts.Chart({
        chart: chart[2],
        series: series[2],
        title: title[2],
        xAxis: xA[2],
        yAxis: yA[2]
        
    });
    light = new Highcharts.Chart({
        chart: chart[3],
        series: series[3],
        title: title[3],
        xAxis: xA[3],
        yAxis: yA[3]
        
    });

    setInterval(requestData,1000);
});