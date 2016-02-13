queue()
    .defer(d3.json, "/dashboards/threats/")
    .await(makeGraphs);

function makeGraphs(error, threatsJson) {
    
    // Clean threatsJson data
    var threatsProject = threatsJson;
    var dateFormat = d3.time.format("%Y-%m-%d")

    threatsProject.forEach(function(d) {
        d["timestamp"] = dateFormat.parse(d["timestamp"]);
    });

    // Create a Crossfilter instance
    var ndx = crossfilter(threatsProject);

    //i Define Dimensions
    var dateDim = ndx.dimension(function(d) { return d["timestamp"]; });
    var threatsDim = ndx.dimension(function(d) { return d["category"]; });
    var subjectDim = ndx.dimension(function(d) { return d["subject"]; });
    var userAgentDim = ndx.dimension(function(d) { return d["user_agent"]; });
    var hostnameDim = ndx.dimension(function(d) { return d["hostname"]; });
    var statusDim = ndx.dimension(function(d) { return d["status"]; });
    var protocolDim = ndx.dimension(function(d) { return d["protocol"]; });

    // Group and calculate metrics.
    var numEventsByDate = dateDim.group(); 
    var numEventsByThreats = threatsDim.group();
    var numEventsBySubject = subjectDim.group();
    var numEventsByUserAgent = userAgentDim.group();
    var numEventsByHostname = hostnameDim.group();
    var numEventsByProtocol = protocolDim.group();

    // Calculate groups.
    var statusGroup = statusDim.group()
    var all = ndx.groupAll();

    // Define values (to be used in charts).
    var minDate = dateDim.bottom(1)[0]["timestamp"];
    var maxDate = dateDim.top(1)[0]["timestamp"];

    // Charts.
    var timeChart = dc.lineChart("#time-chart");
    var threatsChart = dc.rowChart("#threats-row-chart");
    var subjectChart = dc.rowChart("#subject-row-chart");
    var userAgentChart = dc.rowChart("#user-agent-row-chart");
    var hostnameChart = dc.rowChart("#hostname-row-chart");
    var numberEventsND = dc.numberDisplay("#number-events-nd")
    var protocolPie = dc.pieChart("#protocol-pie")

    dc.dataCount("#row-selection")
        .dimension(ndx)
        .group(all);

    selectEvent = dc.selectMenu('#menu-select')
        .dimension(statusDim)
        .group(statusGroup);

    numberEventsND
        .formatNumber(d3.format("d"))
        .valueAccessor(function(d){return d; })
        .group(all);

    timeChart
        .width(1850)
        .height(200)
        .margins({top: 10, right: 50, bottom: 30, left: 50})
        .dimension(dateDim)
        .group(numEventsByDate)
        .transitionDuration(500)
        .x(d3.time.scale().domain([minDate, maxDate]))
        .elasticY(true)
        .xAxisLabel("Date")
        .yAxis().ticks(4);

    threatsChart
        .width(700)
        .height(180)
        .dimension(threatsDim)
        .group(numEventsByThreats)
        .xAxis().ticks(4);

    subjectChart
        .width(600)
        .height(350)
        .dimension(subjectDim)
        .group(numEventsBySubject)
        .xAxis().ticks(4);

    protocolPie
        .width(450)
        .height(180)
        .innerRadius(35)
        .dimension(protocolDim)
        .group(numEventsByProtocol);

    userAgentChart
        .width(600)
        .height(350)
        .dimension(userAgentDim)
        .group(numEventsByUserAgent)
        .xAxis().ticks(4);

    hostnameChart
        .width(600)
        .height(350)
        .dimension(hostnameDim)
        .group(numEventsByHostname)
        .xAxis().ticks(4);

    dc.renderAll();

};

