var screenWidth = screen.width;
var screenHeight = screen.height;
var snowbg = null;
var snowbgHeight = 0;
var snowbgWidth = 0;
var SNOW_MAX_COUNT = 30; //雪花总数
var currCount = 0;
var snowIds = new Array();
var NO_USE = 0;
var USING = 1;
var SNOW_BASE_COLOR = "#ddd";

//初始化雪花id
function initIds() {
    for (var i = 0; i < SNOW_MAX_COUNT; i++) {
        snowIds[i] = NO_USE;
    }
}

function getId() {
    var res = -1;
    for (var i = 0; i < SNOW_MAX_COUNT; i++) {
        if (NO_USE == snowIds[i]) {
            res = i;
            break;
        }
    }
    return res;
}

//开始下落
function snowDrop(eleSnow, currPos, id) {
    if (null === eleSnow) {
        console.log("eleSnow is null");
        return;
    }
    var snowSpeed = 3 + parseInt(2 * Math.random());
    var funId = setInterval(function () {
        currPos += snowSpeed;
        eleSnow.style.top = currPos + "px";
        if (currPos > snowbgHeight) {
            snowbg.removeChild(eleSnow);
            snowIds[id] = NO_USE;
            // console.log("eleSnow clearInterva : " + id);
            currCount--;
            clearInterval(funId);
        }
    }, 50);
}

function getRandomColor(rmin, rmax, gmin, gmax, bmin, bmax, a) {
    var r = Math.round(Garden.random(rmin, rmax));
    var g = Math.round(Garden.random(gmin, gmax));
    var b = Math.round(Garden.random(bmin, bmax));
    var limit = 25;
    if ((Math.abs(r - g) <= limit) && (Math.abs(g - b) <= limit) && (Math.abs(b - r) <= limit)) {
        return getRandomColor(rmin, rmax, gmin, gmax, bmin, bmax, a);
    } else if ((r < 128) && (g < 128) && (b < 128)) {
        return getRandomColor(rmin, rmax, gmin, gmax, bmin, bmax, a);
    } else {
        return 'rgba(' + r + ',' + g + ',' + b + ',' + a + ')';
    }
};


//点击雪
function clickSnow(id) {
    eleSnow = document.getElementById("snow" + id);
    if (NO_USE == eleSnow.getAttribute("snowing")) {
        return;
    }
    eleSnow.setAttribute("snowing", NO_USE);
    // eleSnow.style.color = "#fff";
    s_rgba = getRandomColor(0, 255, //
        0, 255, //
        0, 255, //
        1);
    // console.log(s_rgba);
    eleSnow.style.color = s_rgba;// s_rgba;

    var textSize = eleSnow.style.getPropertyValue("font-size");//字体大小(包含px)
    textSize = textSize.substring(0, textSize.length - 2);
    var xPos = eleSnow.getAttribute("posXCenter");//中心坐标
    var poemId = parseInt(Math.random() * poems.length);
    var showText = poems[poemId];
    // alert(showText);
    // textSize = 24 + "pt";
    if (!isMobile()) {
        textSize = 24;
    } else {
        textSize = 20;
    }
    eleSnow.style.fontSize = textSize + "px";
    eleSnow.style.textAlign = "right";
    // console.log("textSize : " + textSize + " , " + showText.length);
    eleSnow.style.marginLeft = parseInt(xPos - textSize * showText.length / 2) + "px";
    eleSnow.innerHTML = showText;

}

//触摸雪
function touchSnow(id) {
    eleSnow = document.getElementById("snow" + id);
    if (NO_USE == eleSnow.getAttribute("snowing")) {
        return;
    }
    eleSnow.style.color = "#fff";
}

//离开雪
function leaveSnow(id) {
    if (NO_USE == eleSnow.getAttribute("snowing")) {
        return;
    }
    eleSnow = document.getElementById("snow" + id);
    eleSnow.style.color = SNOW_BASE_COLOR;
}

function startSingleSnow() {

    var id = getId();
// console.log("get id : " + id + " ids : " + printIds());
    if (id < 0) {
        console.log("get id err");
        return;
    }
    //雪花位置
    var tmpLeft = parseInt(Math.random() * snowbgWidth);

    //雪花属性
    var eleSnow = document.createElement("div");
    var snowSize = 30;
    if (!isMobile()) {
        snowSize = 25 + parseInt(25 * Math.random());
    } else {
        snowSize = 20 + parseInt(20 * Math.random());
    }
    eleSnow.innerHTML = "❅";//'<img src="./pic/snow.png" style="width:{0};height:{1}"></img>'.format(snowSize+"px",snowSize+"px");
    eleSnow.id = "snow" + id;
    eleSnow.setAttribute("onclick", "clickSnow(" + id + ")");
    eleSnow.setAttribute("onmouseover", "touchSnow(" + id + ")");
    eleSnow.setAttribute("onmouseout", "leaveSnow(" + id + ")");
    eleSnow.setAttribute("posXCenter", tmpLeft + snowSize / 2);
    eleSnow.setAttribute("style", 'text-align:center;font-size:{0}px;color:{1};margin-left:{2}px'//
        .format(snowSize, SNOW_BASE_COLOR, tmpLeft));
    eleSnow.setAttribute("snowing", USING);

    eleSnow.style.position = "absolute";
    snowbg.appendChild(eleSnow);

    snowIds[id] = USING;
    // console.log("snowDrop : " + id + " ids : " + printIds());
    currCount++;
    snowDrop(eleSnow, 0, id);
}

var funcIdStartSnow = 0;

function isMobile() {
    var u = navigator.userAgent;
    var isAndroid = u.indexOf('Android') > -1 || u.indexOf('Adr') > -1; //android终端
    var isiOS = !!u.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/); //ios终端
    if ((true == isiOS) || (true == isAndroid)) {
        return true;
    } else {
        return false;
    }
}

function startSnow() {
    if (isMobile()) {
        SNOW_BASE_COLOR = "#fff";
    }

    var snowSpeed = 1; //设置下雪的速度，越大雪花越多，下的越快
    snowbg = document.getElementById('snowbg');
    snowbgHeight = $(snowbg).height();
    snowbgWidth = $(snowbg).width();
    // console.log("snowbg : " + snowbgHeight + " , " + snowbgWidth);
    initIds();
    clearInterval(funcIdStartSnow);

    funcIdStartSnow = setInterval(function () {
        if (currCount < SNOW_MAX_COUNT) {
            startSingleSnow();
        }
    }, 100);
}
