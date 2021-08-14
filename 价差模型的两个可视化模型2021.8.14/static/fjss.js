


// getJSON(url,作用的返回内容)  # 接口单项请求请求成功
$.getJSON('http://127.0.0.1:5000/fjss',function (content) {
    D_T = content.data;

     var chart = Highcharts.chart('container', {
       title: {
           text: '可视化测试'
       },
       subtitle: {
           text: '数据来源：本地mysql'
       },
       yAxis: {
           title: {
               text: '收益率'
           }
       },
       legend: {
           layout: 'vertical',
           align: 'right',
           verticalAlign: 'middle'
       },
       plotOptions: {
           series: {
               label: {
                   connectorAllowed: false
               }
               // pointStart: 2010
           }
       },
       series: [{
           name: '可视化测试',
           data:D_T,
           //　数据量太大这种方法就失效了！
       }],
       responsive: {
           rules: [{
//               condition: {
//                   maxWidth: 500
//               },
               chartOptions: {
                   legend: {
                       layout: 'horizontal',
                       align: 'center',
                       verticalAlign: 'bottom'
                   }
               }
           }]
       }
});})



