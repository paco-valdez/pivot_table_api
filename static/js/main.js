var pivots = {
  "columns":["STAT_PROFILE_DATE_YEAR", "STAT_PROFILE_DATE_MONTH", "STATE_ABBR"],
  "rows":["PROD_LINE", "AGENCY_ID", "PROD_ABBR", "STATE_ABBR"],
  "values": {
    "sum":["RETENTION_POLY_QTY", "WRTN_PREM_AMT", "LOSS_RATIO"],
    "mean":["RETENTION_POLY_QTY", "WRTN_PREM_AMT", "LOSS_RATIO"]
  },
  "reports": ["AGENCY_ID", "PROD_LINE"]
};


function get_dataset(dataset) {
    $.ajax({
        url: "https://demo:demo@re291hwt17.execute-api.us-west-1.amazonaws.com/dev/dataset/"+dataset,
        beforeSend: function (xhr) {
            xhr.setRequestHeader ("Authorization", "Basic " + btoa("demo:demo"));
        }
    }).done(function (data) {
        if (console && console.log) {
            console.log(data);
            chart = generate(data);
        }
    });
}


var padding = {}, types = {};
var generate = function (response) {
    var columns = [response.data.columns];
    columns = columns.concat(response.data.data);
    if (columns.length > 10){
        columns = columns.slice(0, 11);
    }

    console.log(columns);
    return c3.generate({
        data: {
            x: columns[0][0],
            columns: columns,
            type: 'bar'
        },
        axis: {
            x: {
                type: 'category',
                tick: {
                    rotate: 75,
                    multiline: false
                },
                height: 130
            }
        }
    });
};
var chart;
get_dataset('sum-RETENTION_POLY_QTY-PROD_LINE-STAT_PROFILE_DATE_YEAR');

var update_dataset = function () {
    var row = $("#rows").val();
    var column = $("#columns").val();
    var value = $("#values").val();
    var func = $("#func").val();
    var key = [func, value, row, column].join('-');
    $("#download").attr('href', 'https://s3-us-west-1.amazonaws.com/datasets-hruncx1gi/' + key + '.csv' );
    get_dataset(key);
};
$('select').on('change', function() {
    update_dataset();
});


