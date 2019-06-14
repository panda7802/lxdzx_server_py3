//一般直接写在一个js文件中
layui.use(['layer', 'form'], function(){
  var layer = layui.layer
  ,form = layui.form;

  // layer.msg('Hello World');
});

//数据存储
layui.data('test', {
  key: 'nickname',
  value: '贤心'
});

var localTest = layui.data('test');
console.log(localTest.nickname); //获得“贤心”

// 设备信息
var device = layui.device("aaa");
console.log(device);

