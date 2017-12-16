var pivots = {
  "columns":["STAT_PROFILE_DATE_YEAR", "STAT_PROFILE_DATE_MONTH", "STATE_ABBR"],
  "rows":["PROD_LINE", "AGENCY_ID", "PROD_ABBR", "STATE_ABBR"],
  "values": {
    "sum":["RETENTION_POLY_QTY", "WRTN_PREM_AMT", "LOSS_RATIO"],
    "mean":["RETENTION_POLY_QTY", "WRTN_PREM_AMT", "LOSS_RATIO"]
  },
  "reports": ["AGENCY_ID", "PROD_LINE"]
};


var padding = {}, types = {};
  var generate = function () { return c3.generate({
    data: {
      x: 'x',
      columns: [
        ['x', ],
        ['data1', ],
        ['data2', ],
//            ['x', '2013-01-01', '2013-01-02', '2013-01-03', '2013-01-10', '2013-01-11', '2013-01-12'],
//            ['data1', 30, 200, 100, 400, 150, 250],
//            ['data2', 310, 400, 200, 100, 450, 150],
//            ['data3', 310, 400, 200, 100, null, 150],
      ],
      types: types,
//          labels: true
    },
    bar: {
      width: 10
    },
    axis: {
      x: {
        type: 'timeseries',
        tick: {
          format: '%m/%d',
        },
        padding: padding
      },
      y: {
/*
        min: -100,
        max: 1000
*/
      }
    },
/* not supported yet
    grid: {
      x: {
        show: true
      },
      y: {
        show: true
      }
    }
*/
  }); }, chart;
function run() {
  chart = generate();
  setTimeout(function () {
    chart.flow({
      columns: [
        ['x', '2013-01-21'],
        ['data1', 500],
        ['data3', 200],
      ],
      duration: 1500
    });
  }, 1000);
  setTimeout(function () {
    chart.flow({
      columns: [
        ['x', '2013-02-01', '2013-02-08', '2013-02-15'],
        ['data1', 200, 400, 300],
        ['data2', 100, 300, 200],
        ['data3', 100, 200, 50]
      ],
      length: 1,
      duration: 1500
    });
  }, 4000);
  setTimeout(function () {
    console.log("Flow 1");
    chart.flow({
      columns: [
        ['x', '2013-03-01', '2013-03-08'],
        ['data1', 200, 500],
        ['data2', 300, 400],
        ['data3', 400, 200]
      ],
      to: '2013-02-08',
      duration: 1500
    });
  }, 7000);
  setTimeout(function () {
    chart.flow({
      columns: [
        ['x', '2013-03-15', '2013-05-01'],
        ['data1', 200, 500],
        ['data2', 300, 400],
        ['data3', 400, 200]
      ],
      length: 0,
      duration: 1500
    });
  }, 10000);
  setTimeout(function () {
    chart = generate();
  }, 14000);
  setTimeout(function () {
    chart.flow({
      columns: [
        ['x', '2013-01-21', '2013-01-25', '2013-01-26'],
        ['data1', 500, 300, 100],
        ['data3', 200, 150, null],
      ],
      duration: 1500
    });
  }, 15000);
  setTimeout(function () {
    chart.flow({
      columns: [
        ['x', '2013-02-01'],
        ['data1', 200],
        ['data2', 100],
        ['data3', 100]
      ],
      length: 0,
      duration: 1500
    });
  }, 18000);
  setTimeout(function () {
    chart.flow({
      columns: [
        ['x', '2013-03-01'],
        ['data1', 200],
        ['data2', 300],
        ['data3', 400]
      ],
      to: '2013-02-01',
      duration: 1500
    });
  }, 21000);
};
run();
setTimeout(function () {
  padding = {left: 0, right: 0};
  run();
}, 25000);
setTimeout(function () {
  types = {
    data2: 'area',
    data3: 'bar',
  }
  run();
}, 50000);
