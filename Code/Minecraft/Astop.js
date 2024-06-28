//作者 umaru rize
//只发布在minebbs.com

const lang_path = './plugins/Astop/lang.json'
const config_path = './plugins/Astop/config.json'
const lang = data.openConfig(lang_path,'json','{}')
const config = data.openConfig(config_path,'json','{}')

if(lang.get('command') == null){
    lang.set('command','astop')
    lang.set('title1','Astop')
    lang.set('title2','Astop-confirm')
    lang.set('title3','Astop-maintenance')
    lang.set('content1','选择操作')
    lang.set('content2','确定关服吗？')
    lang.set('content3','选择操作')
    lang.set('notice1','服务器已关闭')
    lang.set('notice2','服务器正在维护中..')
    lang.set('mainformimage1','textures/ui/promo_chicken')
    lang.set('mainformimage2','textures/ui/icon_recipe_equipment')
    lang.set('stopimage1','')
    lang.set('stopimage2','')
    lang.set('mimage1','')
    lang.set('mimage2','')
    lang.set('mimage3','')
}
let command = lang.get('command')
let title1 = lang.get('title1')
let title2 = lang.get('title2')
let title3 = lang.get('title3')
let content1 = lang.get('content1')
let content2 = lang.get('content2')
let content3= lang.get('content3')
let notice1 = lang.get('notice1')
let notice2 = lang.get('notice2')
let mainformimage1 = lang.get('mainformimage1')
let mainformimage2 = lang.get('mainformimage2')
let stopimage1 = lang.get('stopimage1')
let stopimage2 = lang.get('stopimage2')
let mimage1 = lang.get('mimage1')
let mimage2 = lang.get('mimage2')
let mimage3 = lang.get('mimage3')

if(config.get('kickall') == null){
    config.set('kickall',0)
}
let kickall = config.get('kickall')

load()
function mainform(){
    var fm = mc.newSimpleForm()
    fm.setTitle(title1)
    fm.setContent(content1)
    fm.addButton("关闭服务器",mainformimage1)
    fm.addButton("维护服务器",mainformimage2)
    return fm
}

function domainform(pl,choose){
    if(choose == null) return
    if(choose== 0){
        pl.sendForm(stop(),dostop)
    }
    if(choose == 1){
        pl.sendForm(maintenance(),domaintenance)
    }
}

function stop(){
    var sfm = mc.newSimpleForm()
    sfm.setTitle(title2)
    sfm.setContent(content2)
    sfm.addButton("确认关闭服务器",stopimage1)
    sfm.addButton("点错了awa",stopimage2)
    return sfm
}

function dostop(pl,schoose){
    if(schoose == null) return
    if(schoose == 0){
        setTimeout(function(){mc.broadcast("服务器将于15秒后关闭")},1000)
        setTimeout(function(){mc.broadcast("服务器将于10秒后关闭")},5000)
        setTimeout(function(){mc.broadcast("服务器将于5秒后关闭")},10000)
        setTimeout(function(){
            mc.getOnlinePlayers().forEach(pl =>{
                pl.kick(notice1)
            })
            mc.runcmd('stop')  
        },15000)
        return
    }
    if(schoose == 1){
        return
    }
}
function maintenance(){
    var mfm = mc.newSimpleForm()
    mfm.setTitle(title3)
    mfm.setContent(content3)
    mfm.addButton("开始维护",mimage1)
    mfm.addButton("开放服务器",mimage2)
    mfm.addButton("我再想想",mimage3)
    return mfm
}

function domaintenance(pl,mchoose){
    if(mchoose == null) return
    if(mchoose == 0){
        setTimeout(function(){mc.broadcast("服务器将于15秒后维护")},1000)
        setTimeout(function(){mc.broadcast("服务器将于10秒后维护")},5000)
        setTimeout(function(){mc.broadcast("服务器将于5秒后维护")},10000)
        setTimeout(function(){
        pl.tell("服务器已进入维护状态")   
        config.set("kickall",1)
        kickall = config.get('kickall')
        mc.getOnlinePlayers().forEach(pl => {
                if (!pl.isOP())
                    pl.kick(notice2)
            })},15000)
        }
       if(mchoose == 1){
           pl.tell("服务器已对玩家开放")
           config.set("kickall",0)
           kickall = config.get('kickall') 
        }
        if(mchoose == 2){
            return null
        }
    }




function load(){
        mc.regPlayerCmd(command,"open Astop gui",function(pl){
            if(pl.isOP()){
            pl.sendForm(mainform(),domainform)}
            if(!pl.isOP()){
                pl.tell("你没有权限打开此表单")
            }
     })
}

mc.listen('onPreJoin',(pl) => {
 if(kickall == 1){
    if(!pl.isOP()) {
        pl.kick(notice2)
        return true
    }}
if(kickall == 0){return null}
})

logger.log("[Astop]加载成功")
logger.log("[作者]umaru rize--v0.1")