
window.onload = function () {

    wheels = new wheelnav('wheelDiv');
    wheels.slicePathFunction = slicePath().CogBasePieSlice;
    wheels.markerPathFunction = markerPath().DropMarker;
    wheels.clickModeRotate = true;
    wheels.markerPathFunction = markerPath().DropMarker;
    wheels.markerAttr = { fill: '#213CA7', stroke: '#213CA7', };
    wheels.markerEnable = true;
    wheels.createWheel(['finanse', 'planowanie', 'grupy', 'odnosniki', 'platnosci']);
    wheels.spreaderInTitle = 'planowanie';
    wheels.navItems[0].navigateFunction = function () {show_buttons_finance()};
    wheels.navItems[1].navigateFunction = function () { show_time_table() };
    wheels.navItems[2].navigateFunction = function () { show_buttons() };
    wheels.navItems[3].navigateFunction= function () {  show_link() };
    wheels.navItems[4].navigateFunction = function () {  Payments() };
       //Insert generated JavaScript code from here -> http://pmg.softwaretailoring.net

};

