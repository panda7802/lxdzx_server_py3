function fresh() {

    if (location.href.indexOf("&reload=true") < 0) {
        location.href += "&reload=true";
    }
}

var flushed = false;

function xnjy_init() {
    // var ui_type = get_query_string("ui_type", 1);
    // if (0 !== ui_type) {
    //     document.body.style.background = "#ffc703";
    // } else {
    //     document.body.style.background = "#0303ff";
    // }

	var back_color = document.body.style.background;
	
	//var COLORS = ["#ffc703","#0303ff"];
	//if(!$.inArray(back_color, COLORS)||(0==back_color.length)) {
    document.body.style.background = "#ffc703";
	//}

    var bl = 1.0;
    var back = document.getElementById('div_back');
    var back_height = $(back).height();
    var back_width = $(back).width();
    bl = back_height / 1920.0;

    var img_back = document.getElementById('img_back');
    img_back.style.height = back_height + "px";
    img_back.style.width = back_height * 0.5625 + "px";
    //img_back.style.width = "100%";

    var div_cont = document.getElementById('div_cont');
    div_cont.style.height = back_height + "px";
    //div_cont.style.width = "100%";
    div_cont.style.width = back_height * 0.5625 + "px";
    div_cont.style.marginLeft = (back_width - back_height * 0.5625 ) / 2 + "px";


    //setTimeout("fresh()",1000)
    if (!flushed) {
        setTimeout("xnjy_init()", 1000);
        flushed = true;
    }
}

var share_title = "我的时间胶囊";
var share_pic = "https://www.pandafly.cn/static/img/xnjy/icon.jpg";
var share_desc = "留学的真相-我的时间胶囊";
var share_link = window.location.href;


/**
 *微信分享
 */
function jssdk_share() {
	console.log("init share");
	var base_path = "http://www.pandafly.cn/";
    $(function () {
        /***用户点击分享到微信圈后加载接口接口*******/
        var url = window.location.href.split('#')[0];
	//	url = url.split('?')[0];
	//	url = decodeURIComponent(url);
	//	alert(url);
        var send_url = base_path + "lxdzx/xnjyshare?url=" +encodeURI(url);// + encodeURIComponent(url);
//		alert(url);
//		alert(send_url);
        console.log("url:" + send_url);
        $.ajax({
            url: send_url,
			data:'',
            type: "Get",
            async: true,
            cache: false,
            dataType: "json",
            success: function (data) {
                wx.config({
                   debug: false,
                   appId: 'wxaa3e9bee4d1d172d',
 //                   appId: 'wx29db0e2cd630f115',
                    timestamp: data.timeStamp,
                    nonceStr: data.nonceStr,
                    signature: data.signature,
                    jsApiList: [
                        'checkJsApi',
                        'onMenuShareTimeline',
                        'hideOptionMenu',
                        'onMenuShareAppMessage'
                    ]
                });
                wx.error(function (res) {
                    console.error("wx err");
                });
                wx.ready(function () {
                    console.log("ready");
                    //wx.hideOptionMenu();/***隐藏分享菜单****/
                    wx.checkJsApi({
                        jsApiList: [
                            'getLocation',
                            'onMenuShareTimeline',
                            'onMenuShareAppMessage'
                        ],
                        success: function (res) {
							console.log(res);
                            //alert(res.errMsg);
                        }
                    });

                    wx.onMenuShareAppMessage({
                        title: share_title,
                        desc: share_desc,
                        link: share_link,
                        imgUrl:share_pic,
                        trigger: function (res) {
                            //alert('用户点击发送给朋友');
                        },
                        success: function (res) {
                            
                        },
                        cancel: function (res) {
                            //alert('已取消');
                        },
                        fail: function (res) {
                            alert(res.errMsg);
                        }
                    });

                    // 2.2 监听“分享到朋友圈”按钮点击、自定义分享内容及分享结果接口
                    wx.onMenuShareTimeline({
                        title: share_title,
                        desc: share_desc,
                        link: share_link,
                        imgUrl:share_pic,
                        trigger: function (res) {
                            //alert('用户点击分享到朋友圈');
                        },
                        success: function (res) {
                          //  alert("share succ");
                            //分享之后增加游戏次数
                        },
						complete: function (res) {
						//	alert(e);
                         },
                        cancel: function (res) {
                          //  alert('已取消');
                        },
                        fail: function (res) {
                            alert(res.errMsg);
                        }
                    });

                    wx.error(function (res) {
                        alert(res.errMsg);
                    });
                });
            },
            error: function () {
                alert('ajax request failed!!!!');
                return;
            }
        });
    });
}

