/**
 *微信的功能
 */

var wx_share_title = "我们";
var wx_share_pic = "https://www.pandafly.cn/static/img/love/rose.jpeg";
var wx_share_desc = "我们的点点滴滴";
var wx_share_link = window.location.href;


/**
 *微信分享
 */
function jssdk_share() {
    console.log("init share");
    var base_path = "http://www.pandafly.cn/";
    $(function () {
        /***用户点击分享到微信圈后加载接口接口*******/
        var url = window.location.href.split('#')[0];
        var send_url = base_path + "lxdzx/xnjyshare?url=" + encodeURI(url);// + encodeURIComponent(url);
        // console.log(send_url)
        $.ajax({
            url: send_url,
            data: '',
            type: "Get",
            async: true,
            cache: false,
            dataType: "json",
            success: function (data) {
                wx.config({
                    debug: false,
                    appId: 'wxaa3e9bee4d1d172d',
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
                        }
                    });

                    wx.onMenuShareAppMessage({
                        title: wx_share_title,
                        desc: wx_share_desc,
                        link: wx_share_link,
                        imgUrl: wx_share_pic,
                        trigger: function (res) {//用户点击分享到朋友圈
                        },
                        success: function (res) {
                        },
                        cancel: function (res) {
                        },
                        fail: function (res) {
                        }
                    });

                    // 2.2 监听“分享到朋友圈”按钮点击、自定义分享内容及分享结果接口
                    wx.onMenuShareTimeline({
                        title: wx_share_title,
                        desc: wx_share_desc,
                        link: wx_share_link,
                        imgUrl: wx_share_pic,
                        trigger: function (res) {//用户点击分享到朋友圈
                            //alert('');
                        },
                        success: function (res) {
                        },
                        complete: function (res) {
                        },
                        cancel: function (res) {
                        },
                        fail: function (res) {
                        }
                    });

                    wx.error(function (res) {
                    });
                });
            },
            error: function () {//初始化分享失败
                return;
            }
        });
    });
}
