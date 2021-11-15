var myChart1 = echarts.init(document.getElementById('main'));
var option;
myChart.showLoading();
$.get('./china/china.json', function (geoJson) {
    console.log("as");
    var myChart = echarts.init(document.getElementById('main'));
    myChart.hideLoading();
    echarts.registerMap('china', geoJson);
    option = {
        backgroundColor: '#2c343c',//画布背景颜色
        title: {  //标题样式
            text: '工资分布',
            x: "center",
            y: "6%",
            textStyle: {
                fontSize: 18,
                color: "rgba(255, 255, 255,0.5)"
            },
        },
        tooltip: {  //这里设置提示框
            trigger: 'item',  //数据项图形触发
            backgroundColor: "rgba(255, 255, 255)",  //提示框浮层的背景颜色。
            //字符串模板(地图): {a}（系列名称），{b}（区域名称），{c}（合并数值）,{d}（无）
            formatter: '地区：{b}<br/>平均工资：{c}'
        },
        visualMap: {//视觉映射组件
            top: '42%',
            right: '3%',
            min: 3000,
            max: 500000,
            textStyle: {
                color: '#eee'
            },
            text: ['High', 'Low'],
            realtime: true,  //拖拽时，是否实时更新
            calculable: true,  //是否显示拖拽用的手柄
            inRange: {
                color: ['rgb(78, 163, 151)', 'rgb(34, 195, 170)', 'rgb(123, 217, 165)']
            }
        },
        series: [
            {
                name: '工资分布',
                type: 'map',
                map: 'china',
                left: "36%",
                bottom: "-40%",
                roam: false,//是否开启鼠标缩放和平移漫游
                itemStyle: {//地图区域的多边形 图形样式
                    normal: {//是图形在默认状态下的样式
                        areaColor: '#2c343c',
                        borderColor: '#0096cb',
                        borderWidth: 1,
                        label: {
                            show: false, //是否显示地图省份得名称
                            color: "#fff",
                            fontSize: 10,
                            fontFamily: "Arial",
                        }
                    },
                    emphasis: {
                        borderWidth: 1.5,//鼠标滑过区域，区域边框宽度
                        borderColor: '#fff',//鼠标滑过区域，区域边框颜色
                        areaColor: "rgb(78, 163, 151)",//鼠标滑过区域背景色
                        label: {
                            //动态展示的样式
                            show: true, //是否显示地图省份得名称
                            color: "#fff",
                            fontSize: 15,
                            fontFamily: "Arial",
                        }
                    }
                },
                zoom: 1,  //地图缩放比例,默认为1
                emphasis: {//是图形在高亮状态下的样式,比如在鼠标悬浮或者图例联动高亮时
                    areaColor: "rgb(78, 163, 151)",
                    color: "#fff"
                },
                top: "3%",//组件距离容器的距离
                data: [],
                label: {
                    show: false
                },
            }
        ],
    }
         var option1 = {
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {c} ({d}%)"
        },

        series: [
          {
            name: "类型",
            type: "pie",
            radius: [10, 100],
            center: ["55%", "40%"],
            roseType: "area",
            data: [
              { value: 10, name: "rose1" },
              { value: 5, name: "rose2" },
              { value: 15, name: "rose3" },
              { value: 20, name: "rose4" }
            ],
            itemStyle: {
              color: 'rgb(78, 163, 151)',
              shadowBlur: 100,
              shadowColor: 'rgba(0, 0, 0, 0.5)'
            },
              animationType: 'scale',
              animationEasing: 'elasticOut',
              animationDelay: function(idx) {
                 return Math.random() * 200;
                 },
          }
        ],
      };
         myChart1.setOption(option);
});

// // 基于准备好的dom，初始化echarts实例
//
// var myChart2 = echarts.init(document.getElementById('calltrend_view2'));
// // 指定图表的配置项和数据
//
//
//        // 1. 实例化对象
// // var myChart = echarts.init(document.querySelector("#bar"));
// // 2. 指定配置和数据
// var option2 = {
//     color: ['rgb(78, 163, 151)'],
//     // 工具提示
//     tooltip: {
//       // 触发类型  经过轴触发axis  经过轴触发item
//       trigger: 'axis',
//       // 轴触发提示才有效
//       axisPointer: {
//         // 默认为直线，可选为：'line' 线效果 | 'shadow' 阴影效果
//         type: 'shadow'
//       }
//     },
//     // 图表边界控制
//     grid: {
//       // 距离 上右下左 的距离
//       left: '3%',
//       right: '4%',
//       bottom: '3%',
//       // 是否包含文本
//       containLabel: true
//     },
//     // 控制x轴
//     xAxis: [
//       {
//         // 使用数据的值设为刻度文字
//         type: 'value'
//       }
//     ],
//     // 控制y轴
//     yAxis: [
//         {
//             // 使用类目，必须有data属性
//             type: 'category',
//             // 使用 data 中的数据设为刻度文字
//             data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
//             // 刻度设置
//             axisTick: {
//                 // true意思：图形在刻度中间
//                 // false意思：图形在刻度之间
//                 alignWithLabel: true
//             }
//         }
//     ],
//     legend: {
//         show:true,
//         left:'20%',
//         top:'30%',
//         data: ["2020年"],
//     },
//     // 控制x轴
//     series: [
//       {
//         // 图表数据名称
//         name: '用户统计',
//         // 图表类型
//         type: 'bar',
//         // 柱子宽度
//         barWidth: '60%',
//         // 数据
//         data: [10, 52, 200, 334, 390, 330, 220]
//       }
//     ]
//   };
//
// // 使用刚指定的配置项和数据显示图表。
// myChart.setOption(option);
// myChart1.setOption(option1);
// myChart2.setOption(option2);
// // myChart.connect([myChart1,myChart2]);
//
// setTimeout(function (){
//     window.onresize = function () {
//         myChart.resize();
//
//     }
// },200)
//
// myChart1.resize();
// myChart2.resize();



