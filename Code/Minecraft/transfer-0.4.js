
//只发布在minebbs
//作者umaru rize

const config_path = './plugins/transfer/config.json'


if(file.exists(config_path)==false){
file.writeTo(config_path,JSON.stringify({notice:"{player}正在跨服",title: "跨服传送表单",content: "选择操作",servers: [{image:"textures/items/apple",name: "服务器1",ip: "abc",port: 12345},{image:"",name: "服务器2",ip: "def",port: 56789}]},null,'\t'))
}

const data = JSON.parse(file.readFrom(config_path))

let title = data.title
let content = data.content
let notice = data.notice

var servers = new Array()
load()
function transfer(){
    var fm = mc.newSimpleForm()
    fm.setTitle(title)
    fm.setContent(content)
    for(var i=0;i<data.servers.length;i++){
    if(data.servers[i].name !=null){
    fm.addButton(data.servers[i].name,data.servers[i].image)}
}
    return fm
}

function tick(pl,id){
    if(id== null)return
    mc.broadcast(notice
        .replace("{player}",pl.realName)
        )
    var choose = data.servers[id]
    pl.transServer(choose.ip,choose.port)
}

function load(){
    mc.regPlayerCmd("tr","Open gui transfer",function(pl){
        pl.sendForm(transfer(),tick)
    })
}

logger.log("[Transfer]加载成功")
logger.log("[作者]umaru rize--v0.4")