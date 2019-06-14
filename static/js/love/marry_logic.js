function goto_show() {
    document.getElementById("future").style.display = "inline";
}

function start_love() {
    offsetX = $("#loveHeart").width() / 2;
    offsetY = $("#loveHeart").height() / 2 - 55;
    together = new Date();
    together.setFullYear(2018, 0, 18);
    together.setHours(11);
    together.setMinutes(45);
    together.setSeconds(0);
    together.setMilliseconds(0);

    if (!document.createElement('canvas').getContext) {
        var msg = document.createElement("div");
        msg.id = "errorMsg";
        msg.innerHTML = "Your browser doesn't support HTML5!<br/>Recommend use Chrome 14+/IE 9+/Firefox 7+/Safari 4+";
        document.body.appendChild(msg);
        document.execCommand("stop");
    } else {
        setTimeout(function () {
            startHeartAnimation();
        }, 500);

        timeElapse(together);
        setInterval(function () {
            timeElapse(together);
        }, 500);

        adjustCodePosition();
        $("#code").typewriter();
    }
}

var UNIT_DAY = "<span class='item_unit'> 天 </span>";
var UNIT_HOUR = "<span class='item_unit'> 小时 </span>";
var UNIT_MIN = "<span class='item_unit'> 分钟 </span>";
var UNIT_SECOND = "<span class='item_unit'> 秒 </span>";
var UNIT_PASSED = "<span class='item_unit'>已经过去 </span>";
var UNIT_LIMIT = "<span class='item_unit'>还有 </span>";

/**
 *  计时
 * @param time_id
 * @param timestamp2
 */
function item_count_time(time_id, timestamp2) {
    var time_item = document.getElementById("far" + time_id);
    var date3 = parseInt((new Date()).getTime() - timestamp2);
    //显示时间
    var days = parseInt(date3 / (1000.0 * 60 * 60 * 24)); //Math.abs((date1.getDate() - date2.getDate()));
    //计算出小时数
    var leave1 = date3 % (24 * 3600 * 1000);   //计算天数后剩余的毫秒数
    var hours = Math.floor(leave1 / (3600 * 1000));
    if (hours < 10) {
        hours = "0" + hours;
    }
    //计算相差分钟数
    var leave2 = leave1 % (3600 * 1000);    //计算小时数后剩余的毫秒数
    var minutes = Math.floor(leave2 / (60 * 1000));
    if (minutes < 10) {
        minutes = "0" + minutes;
    }
    var leave3 = leave2 % (60 * 1000) - 1;
    var seconds = Math.round(leave3 / 1000);
    if (seconds < 10) {
        seconds = "0" + seconds;
    }
    var sfix = date3 > 0 ? UNIT_PASSED : UNIT_LIMIT;
    time_item.innerHTML = "<div id='limit_" + time_id + "' class='item_num'>" //
        + sfix + days + UNIT_DAY
        + hours + UNIT_HOUR
        + minutes + UNIT_MIN
        + seconds + UNIT_SECOND//
        + "</div>";
    if (document.getElementById("us_record").style.display != "none") {
        setTimeout("item_count_time(" + time_id + "," + timestamp2 + ")", 1000);
    }

}

function init_zfys() {
    $.ajax({
        url: "../loveaction/getZfs?parm={}",
        success: function (data) {
            console.log(data);
            data = JSON.parse(data);
            if (data.success) {
                var res = data.data;
                console.log(res);
                if (res.length > 0) {
                    poems = [];
                    for (var key in  res) {
                        if (res[key].name.length > 0) {
                            poems.push(res[key].zf + "<br/>-- " + res[key].name)
                        } else {
                            poems.push(res[key].zf)
                        }
                    }
                }
            }
        }
    });
}

var back_height = 0;
var back_width = 0;

/**
 * 显示背景
 */
function dis_back() {
    $("#img_back").fadeOut(4000, function () {
        show_back();
    });
}

var IMG_COUNT = 86;
var img_index = parseInt(Math.random() * 86);

/**
 * 隐藏背景
 */
function show_back() {
    document.getElementById("img_back").src = "/static/img/love/jhz/" + img_index + ".jpg";
    img_index = (++img_index) % IMG_COUNT;
    $("#img_back").fadeIn(4000, function () {
        setTimeout("dis_back()", 4000);
    });
}

function marry_init() {

    var back = document.getElementById('future');
    back_height = $(back).height();
    back_width = $(back).width();

    if (back_height < back_width) {
        document.getElementById("img_back").style.height = "100%";
        document.getElementById("img_back").style.width = "auto";
    }

    show_back();

    //超时跳转
    goto_show();
    start_love();
    startSnow();

    jssdk_share();

    init_zfys();

}

/**
 * 增加祝福语
 */
function add_zf() {
    var name = prompt("请留下您的姓名:", "");
    if (name.length <= 0) {
        layer.msg('请留下您的姓名');
        return;
    }
    // $.ajax({
    //     url: "../loveaction/getZfByName?parm={\"name\":\"" + name + "\"}",
    //     success: function (data) {
    //         data = JSON.parse(data);
    //         if (data.success) {
    // 祝福语输入
    var zf = prompt("请留下您的祝福:", "");
    var send = "../loveaction/addzf?parm={\"name\":\"" + name + "\",\"zf\":\"" + zf + "\"}";
    if (zf.length <= 0) {
        layer.msg('请留下您的祝福');
        return;
    }
    $.ajax({
        url: send,
        success: function (data) {
            init_zfys();
            layer.msg('谢谢您的祝福，触摸雪花可以看到大家的祝福');
        }
    });
    //         }
    //     }
    // });
    // var layer = layui.layer;
    // // 姓名输入
    // layer.prompt({
    //     formType: 2,
    //     anim: 5,
    //     btnAlign: 'c',//居中
    //     value: name,
    //     title: '请留下您的姓名',
    //     area: ['300px', '140px'] //自定义文本域宽高
    // }, function (value, index, elem) {
    //     document.body.style.zoom = 1;
    //     var name = value;
    //     $.ajax({
    //         url: "../loveaction/getZfByName?parm={\"name\":\"" + name + "\"}",
    //         success: function (data) {
    //             data = JSON.parse(data);
    //             if (data.success) {
    //                 layer.close(index);
    //                 // 祝福语输入
    //                 layer.prompt({
    //                     formType: 2,
    //                     anim: 5,
    //                     btnAlign: 'c',//居中
    //                     value: data.data.zf,
    //                     title: '请留下您的祝福',
    //                     area: ['300px', '140px'] //自定义文本域宽高
    //                 }, function (value, index, elem) {
    //                     var zf = value;
    //                     layer.close(index);
    //                     $.ajax({
    //                         url: "../loveaction/addzf?parm={\"name\":\"" + name + "\",\"zf\":\"" + zf + "\"}",
    //                         success: function (data) {
    //                             document.body.style.zoom = 1;
    //                             document.body.style.cssText += '; -moz-transform: scale(' + size + ');-moz-transform-origin: 0 0; ';
    //                             console.log(data);
    //                             init_zfys();
    //                             layer.msg('谢谢您的祝福，触摸雪花可以看到大家的祝福');
    //                         }
    //                     });
    //                 });
    //             }
    //         }
    //     });
    // });
}