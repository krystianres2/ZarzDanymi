import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc


data = pd.read_csv('reviews_courses.csv', parse_dates=['Timestamp'])

data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')

month_average = data.groupby(['Month', 'Course Name']).mean(numeric_only=True).unstack()
# print(month_average)

data['Weekday'] = data['Timestamp'].dt.strftime('%A')
data['Daynumber'] = data['Timestamp'].dt.strftime('%w')
weekday_average = data.groupby(['Daynumber','Weekday']).mean(numeric_only=True)
weekday_average.sort_values('Daynumber')

print(weekday_average)


chart_def = """{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Changed title',
        align: 'left'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model',
        align: 'left'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Data'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Srednia'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} | {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Srednia wartosc',
        data: [[1, 20], [2, 10], [3, 20]]
    }]
}"""

# chart_def= """
# {
#     chart: {
#         type: 'areaspline'
#     },
#     title: {
#         text: 'Changed title',
#         align: 'left'
#     },
#     subtitle: {
#         text: 'Source: <a href="https://www.ssb.no/jord-skog-jakt-og-fiskeri/jakt" target="_blank">SSB</a>',
#         align: 'left'
#     },
#     legend: {
#         layout: 'vertical',
#         align: 'left',
#         verticalAlign: 'top',
#         x: 120,
#         y: 70,
#         floating: true,
#         borderWidth: 1,
#         backgroundColor:
#             Highcharts.defaultOptions.legend.backgroundColor || '#FFFFFF'
#     },
#     xAxis: {
#         reversed: false,
#         title: {
#             enabled: true,
#             text: 'Data'
#         },
#         labels: {
#             format: '{value}'
#         },
#         accessibility: {
#             rangeDescription: 'Range: 0 to 80 km.'
#         },
#         maxPadding: 0.05,
#         showLastLabel: true
#     },
#     yAxis: {
#         title: {
#             text: 'Srednia'
#         },
#         labels: {
#             format: '{value}°'
#         },
#         accessibility: {
#             rangeDescription: 'Range: -90°C to 20°C.'
#         },
#         lineWidth: 2
#     },
#     tooltip: {
#         shared: true,
#         headerFormat: '<b>Hunting season starting autumn {point.x}</b><br>'
#     },
#     credits: {
#         enabled: false
#     },
#     plotOptions: {
#         series: {
#             pointStart: 2000
#         },
#         areaspline: {
#             fillOpacity: 0
#         }
#     },
#     series: []
# }
# """

def app():
    wp = jp.QuasarPage()

    h1 = jp.QDiv(
        a= wp, text= "Analiza ocen kursów", classes = "text-h3 text-center q-pa-md"
    )

    p1 = jp.QDiv(
        a = wp, text = "Poszczególne wykresy z analizą kursów", classes = "text-h4"
    )

    hc = jp.HighCharts(
        a =wp, options= chart_def
    )

    hc.options.title.text = "Srednia ocen kursow wg MIESIACA"
    hc.options.subtitle.text = "Dane z pliku CSV"

    hc.options.xAxis.categories = list(weekday_average.index.get_level_values(1))
    hc.options.series[0].data= list(weekday_average['Rating'])
    hc.options.series[0].color = "#FFAA00"
    # hc_data =[{
    #     "name":v1,
    #     "data":[v2 for v2 in weekday_average[v1]]}
    #     for v1 in weekday_average.columns]
    # hc.options.series = hc_data

    # hc.options.series[0].data = list(zip(list1,list2))

    return wp


if __name__ == '__main__':
    jp.justpy(app)