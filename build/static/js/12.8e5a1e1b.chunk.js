(this.webpackJsonpblog_front_new=this.webpackJsonpblog_front_new||[]).push([[12],{205:function(e,t,a){},216:function(e,t,a){"use strict";a.r(t),a.d(t,"default",(function(){return d}));var n=a(8),r=a(9),c=a(11),o=a(10),s=a(0),i=a.n(s),l=(a(205),a(35)),u=a(41),m=a.n(u),f=a(34),p=a(46),v=a(225),d=function(e){Object(c.a)(a,e);var t=Object(o.a)(a);function a(){var e;return Object(n.a)(this,a),(e=t.call(this)).state={avatar:"",nickname:"",sign:"",info:""},e}return Object(r.a)(a,[{key:"componentDidMount",value:function(){this.getUserInfo()}},{key:"getUserInfo",value:function(){var e=this,t=this.props.match.params.username;Object(f.g)({username:t}).then((function(t){if(200===t.code){var a=t.data,n=a.nickname,r=a.sign,c=a.info,o=a.avatar;e.setState({nickname:n,sign:r,info:c,avatar:o})}else alert(t.error)}))}},{key:"updateUserInfo",value:function(){var e=this.props.match.params.username,t=this.state,a=t.nickname,n=t.sign,r=t.info;Object(f.t)({nickname:a,sign:n,info:r,username:e}).then((function(e){200===e.code?v.b.success("\u4fee\u6539\u6210\u529f"):v.b.error(e.error)}))}},{key:"uploadPic",value:function(){var e=this,t=this.props.match.params.username,a=this.fileInput.files[0],n=new FormData;n.append("avatar",a),Object(f.u)({username:t,avatar:n}).then((function(t){if(200===t.code){var a=t.data.avatar;e.setState({avatar:a}),e.header.changeAvatar(t.data.avatar);var n=localStorage.getItem("userInfo");(n=JSON.parse(n)).avatar=a,localStorage.setItem("userInfo",JSON.stringify(n)),v.b.success("\u4e0a\u4f20\u6210\u529f")}else v.b.error(t.error)}))}},{key:"previewImg",value:function(e){}},{key:"render",value:function(){var e=this,t=this.state,a=t.avatar,n=t.nickname,r=t.sign,c=t.info;return i.a.createElement("div",{className:"change-info-wrapper"},i.a.createElement(p.a,Object.assign({},this.props,{ref:function(t){return e.header=t}})),i.a.createElement("div",{className:"card col-md-6 change-info"},i.a.createElement("h4",null,"\u4e2a\u4eba\u4fe1\u606f\u4fee\u6539"),i.a.createElement("div",{className:"avatar-wrapper"},i.a.createElement("form",{encType:"multipart/form-data"},i.a.createElement("div",null,i.a.createElement("img",{src:a?l.d+a:m.a,alt:"",className:"userinfo-avatar"})),i.a.createElement("div",{className:"upload-wrapper"},i.a.createElement("label",{htmlFor:"avatar"},"\u4e0a\u4f20\u5934\u50cf:"),i.a.createElement("input",{type:"file",name:"avatar",id:"avatar",style:{color:"#fff"},ref:function(t){return e.fileInput=t},onChange:this.previewImg.bind(this)})),i.a.createElement("button",{type:"button",className:"btn btn-primary",onClick:this.uploadPic.bind(this)},"\u4e0a\u4f20"))),i.a.createElement("div",{className:"info-input-wrapper"},i.a.createElement("div",{className:"info-input-item"},i.a.createElement("label",null,"\u6635\u79f0: "),i.a.createElement("input",{type:"text",className:"nickname form",placeholder:"\u8bf7\u8f93\u5165\u65b0\u7684\u6635\u79f0",value:n,onChange:function(t){return e.setState({nickname:t.target.value})}})),i.a.createElement("div",{className:"info-input-item"},i.a.createElement("label",null,"\u4e2a\u4eba\u7b7e\u540d: "),i.a.createElement("input",{type:"text",className:"sign",placeholder:"\u8bf7\u8f93\u5165\u4e2a\u4eba\u7b7e\u540d",value:r,onChange:function(t){return e.setState({sign:t.target.value})}})),i.a.createElement("div",{className:"info-input-item"},i.a.createElement("textarea",{className:"info",placeholder:"\u8bf7\u8f93\u5165\u4e2a\u4eba\u63cf\u8ff0",value:c,onChange:function(t){return e.setState({info:t.target.value})}})),i.a.createElement("div",{style:{paddingBottom:"30px"}},i.a.createElement("button",{type:"button",value:"\u4fdd\u5b58",className:"btn btn-primary",onClick:this.updateUserInfo.bind(this)},"\u4fdd\u5b58")))))}}]),a}(s.Component)},34:function(e,t,a){"use strict";a.d(t,"i",(function(){return r})),a.d(t,"t",(function(){return c})),a.d(t,"g",(function(){return o})),a.d(t,"u",(function(){return s})),a.d(t,"j",(function(){return i})),a.d(t,"m",(function(){return l})),a.d(t,"s",(function(){return u})),a.d(t,"f",(function(){return m})),a.d(t,"k",(function(){return f})),a.d(t,"n",(function(){return p})),a.d(t,"d",(function(){return v})),a.d(t,"c",(function(){return d})),a.d(t,"a",(function(){return h})),a.d(t,"b",(function(){return b})),a.d(t,"q",(function(){return g})),a.d(t,"e",(function(){return E})),a.d(t,"h",(function(){return k})),a.d(t,"o",(function(){return N})),a.d(t,"r",(function(){return y})),a.d(t,"p",(function(){return O})),a.d(t,"l",(function(){return I}));var n=a(35),r="http://xiaomile.cool/v1";function c(e){return Object(n.f)("".concat(r,"/users/").concat(e.username),e)}function o(e){return Object(n.c)("".concat(r,"/users/").concat(e.username))}function s(e){return Object(n.e)("".concat(r,"/users/").concat(e.username,"/avatar"),e.avatar)}function i(e){return Object(n.e)("".concat(r,"/token"),e)}function l(e){return Object(n.e)("".concat(r,"/topics"),e)}function u(e){return Object(n.f)("".concat(r,"/topics"),e)}function m(e,t){return Object(n.c)("".concat(r,"/topics/").concat(t),e)}function f(e,t,a){return Object(n.e)("".concat(r,"/messages/").concat(t,"/").concat(a),e)}function p(e,t){return Object(n.e)("".concat(r,"/messages/").concat(t),e)}function v(e){return Object(n.b)("".concat(r,"/messages/").concat(e.topicId,"/").concat(e.messageId,"/").concat(e.replyId))}function d(e){return Object(n.b)("".concat(r,"/messages/").concat(e.topicId,"/").concat(e.messageId))}function h(e){return Object(n.e)("".concat(r,"/topics/heart"),e)}function b(e){return Object(n.b)("".concat(r,"/topics/heart"),e)}function g(e,t){return Object(n.c)("".concat(r,"/topics/").concat(t),e)}function E(e,t){return Object(n.b)("".concat(r,"/topics/").concat(t),e)}function k(e){return Object(n.c)("".concat(r,"/topics/home"),e)}function N(){return Object(n.c)("".concat(r,"/topics/view_rank"))}function y(){return Object(n.c)("".concat(r,"/topics/recommend"))}function O(){return Object(n.c)("".concat(r,"/topics/carousel"))}function I(e){return Object(n.c)("".concat(r,"/topics/search"),e)}},35:function(e,t,a){"use strict";a.d(t,"d",(function(){return c})),a.d(t,"c",(function(){return o})),a.d(t,"b",(function(){return s})),a.d(t,"e",(function(){return i})),a.d(t,"f",(function(){return l})),a.d(t,"a",(function(){return u}));var n=a(56),r=a.n(n),c="http://xiaomile.cool/media/";function o(e,t){return new Promise((function(a,n){var c=localStorage.token?localStorage.token:"";r.a.get(e,{params:t,headers:{Authorization:c}}).then((function(e){void 0!==e&&a(e.data)})).catch((function(e){n(e)}))}))}function s(e,t){return new Promise((function(a,n){var c=localStorage.token?localStorage.token:"";r.a.delete(e,{params:t,headers:{Authorization:c}}).then((function(e){a(e.data)})).catch((function(e){n(e)}))}))}function i(e,t){return new Promise((function(a,n){var c=localStorage.token?localStorage.token:"";r.a.post(e,t,{headers:{Authorization:c}}).then((function(e){a(e.data)})).catch((function(e){n(e)}))}))}function l(e,t){return new Promise((function(a,n){var c=localStorage.token?localStorage.token:"";r.a.put(e,t,{headers:{Authorization:c}}).then((function(e){a(e.data)})).catch((function(e){n(e)}))}))}var u=function e(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:0,a=arguments.length>1?arguments[1]:void 0;if(!a)return document.body.scrollTop=document.documentElement.scrollTop=t,t;var n=20,r=a/n,c=document.body.scrollTop+document.documentElement.scrollTop,o=(t-c)/r,s=setInterval((function(){r>0?(r--,e(c+=o)):clearInterval(s)}),n)}},41:function(e,t,a){e.exports=a.p+"static/media/default_avatar.3e2de2c4.jpg"},43:function(e,t,a){},45:function(e,t,a){},46:function(e,t,a){"use strict";a.d(t,"a",(function(){return g}));var n=a(8),r=a(9),c=a(11),o=a(10),s=a(0),i=a.n(s),l=(a(43),a(16)),u=a(223),m=a(225),f=a(95),p=a(34),v=(a(45),function(e){Object(c.a)(a,e);var t=Object(o.a)(a);function a(){var e;return Object(n.a)(this,a),(e=t.call(this)).validate=function(t,a){var n=e.state.registerFormStatus,r=!0;switch(t){case"phone":/^[1][3-9][0-9]{9}$/.test(n[t].value)&&""!==n[t].value?"login"===a&&(n[t].help="",n[t].status="success"):(n[t].help="\u5fc5\u987b\u4e3a\u4e00\u4e2a\u624b\u673a\u53f7\u7801",n[t].status="error",r=!1);break;case"code":"code"!==t&&"captcha"!==t||(6===n[t].value.length?(n[t].status="success",n[t].help=""):(n[t].status="error",n[t].help="\u9a8c\u8bc1\u7801\u4e3a6\u4f4d\u6570",r=!1));break;case"password":n[t].value.length>=6?(n[t].status="success",n[t].help=""):(n[t].status="error",n[t].help="\u5bc6\u7801\u4e0d\u80fd\u5c0f\u4e8e6\u4f4d",r=!1);break;case"confirmPassword":n[t].value===n.password.value&&n[t].value.length>=6?(n[t].status="success",n[t].help=""):(n[t].status="error",n[t].help="\u4e24\u6b21\u5bc6\u7801\u4e0d\u4e00\u81f4",r=!1);break;case"all":e.validate("phone")&&e.validate("password")&&e.validate("code")&&e.validate("confirmPassword")||(r=!1)}return e.setState({registerFormStatus:n}),r},e.login=function(){var t=e.state,a=t.username,n=t.password;Object(p.j)({username:a,password:n}).then((function(t){if(200===t.code){var a=t.data.token;localStorage.setItem("token",a);var n={username:t.username,nickname:t.data.nickname,avatar:t.data.avatar};e.props.setUserInfo(n),localStorage.setItem("userInfo",JSON.stringify(n)),e.props.loginClose(),m.b.success("\u767b\u5f55\u6210\u529f")}else m.b.error(t.error)}))},e.state={username:"",password:""},e}return Object(r.a)(a,[{key:"render",value:function(){var e=this,t=this.state,a=t.username,n=t.password;return i.a.createElement(u.a,{title:"\u767b\u5f55",width:350,visible:this.props.loginVisiable,onCancel:this.props.loginClose,footer:null},i.a.createElement("div",null,i.a.createElement("div",{className:"form-item"},i.a.createElement("span",null,"\u8d26\u53f7\uff1a"),i.a.createElement("input",{type:"text",placeholder:"\u8bf7\u8f93\u5165\u7528\u6237\u540d",className:"form-input",value:a,onChange:function(t){return e.setState({username:t.target.value})}})),i.a.createElement("div",{className:"form-item"},i.a.createElement("span",null,"\u5bc6\u7801\uff1a"),i.a.createElement("input",{type:"password",placeholder:"\u8bf7\u8f93\u5165\u5bc6\u7801",className:"form-input",value:n,onChange:function(t){return e.setState({password:t.target.value})}})),i.a.createElement(f.a,{type:"primary",block:!0,style:{marginBottom:10},loading:this.state.loginLoading,onClick:this.login},"\u767b \u5f55"),i.a.createElement("div",{className:"login-forget"},i.a.createElement("span",null,"\u5fd8\u8bb0\u5bc6\u7801\uff1f"),i.a.createElement("p",null,i.a.createElement("span",null,"\u6ca1\u6709\u8d26\u53f7\uff1f"),i.a.createElement("span",null,"\u6ce8\u518c")))))}}]),a}(s.Component)),d=a(35),h=a(41),b=a.n(h),g=function(e){Object(c.a)(a,e);var t=Object(o.a)(a);function a(){var e;return Object(n.a)(this,a),(e=t.call(this)).state={searchText:"",userInfo:{nickname:"",avatar:""},loginVisiable:!1,current:"mail"},e}return Object(r.a)(a,[{key:"UNSAFE_componentWillMount",value:function(){var e=localStorage.getItem("userInfo");e&&(e=JSON.parse(e),this.setState({userInfo:e}))}},{key:"setUserInfo",value:function(e){this.setState({userInfo:e})}},{key:"logout",value:function(){u.a.confirm({title:"\u63d0\u793a",content:"\u786e\u5b9a\u8981\u9000\u51fa\u767b\u5f55\u5417\uff1f",onOk:function(){localStorage.removeItem("userInfo"),localStorage.removeItem("token"),window.location.href="/"}})}},{key:"changeAvatar",value:function(e){var t=this.state.userInfo;t.avatar=e,this.setState({userInfo:t})}},{key:"toMyList",value:function(){var e=this.state.userInfo;e.username?this.props.history.push("/article/"+e.username):m.b.info("\u8bf7\u5148\u767b\u5f55\uff01")}},{key:"toPushlish",value:function(){this.state.userInfo.username?this.props.history.push("/publish"):m.b.info("\u8bf7\u5148\u767b\u5f55\uff01")}},{key:"onSearch",value:function(){var e=this.state.searchText;if(""!==e.trim()){var t="/search?key="+e;window.open(t,"_blank")}else m.b.info("\u641c\u7d22\u5185\u5bb9\u4e0d\u80fd\u4e3a\u7a7a\uff01",1)}},{key:"render",value:function(){var e=this,t=this.state.userInfo,a=this.state.searchText;return i.a.createElement("nav",{className:"navbar navbar-expand-lg navbar-dark bg-primary"},i.a.createElement("div",{className:"container"},i.a.createElement(l.b,{className:"navbar-brand",to:""},"\u5c0f\u7c73\u4e50"),i.a.createElement("button",{className:"navbar-toggler",type:"button","data-toggle":"collapse","data-target":"#navbarColor01","aria-controls":"navbarColor01","aria-expanded":"false","aria-label":"Toggle navigation"},i.a.createElement("span",{className:"navbar-toggler-icon"})),i.a.createElement("div",{className:"collapse navbar-collapse",id:"navbarColor01"},i.a.createElement("ul",{className:"navbar-nav mr-auto"},i.a.createElement("li",{className:"nav-item"},i.a.createElement(l.b,{className:"nav-link",to:""},"\u9996\u9875 ",i.a.createElement("span",{className:"sr-only"},"(current)"))),i.a.createElement("li",{className:"nav-item",onClick:this.toMyList.bind(this)},i.a.createElement("span",{className:"nav-link"},"\u6211\u7684\u6587\u7ae0")),i.a.createElement("li",{className:"nav-item",onClick:this.toPushlish.bind(this)},i.a.createElement("span",{className:"nav-link"},"\u53d1\u8868\u6587\u7ae0")),i.a.createElement("form",{className:"form-inline ",style:{paddingBottom:0}},i.a.createElement("input",{className:"form-control mr-sm-2",type:"text",placeholder:"\u641c\u7d22",value:a,onChange:function(t){return e.setState({searchText:t.target.value})}}),i.a.createElement("div",{className:"btn btn-secondary my-2 my-sm-0",onClick:this.onSearch.bind(this)},"\u641c\u7d22"))),t.nickname?i.a.createElement("ul",{className:"nav navbar-nav navbar-right"},i.a.createElement("li",{className:"userInfo-wrapper",onClick:function(){return e.props.history.push("/userInfo/".concat(t.username))}},i.a.createElement("span",null," ",i.a.createElement("img",{src:t.avatar?d.d+t.avatar:b.a,alt:"",className:"avatar"})),i.a.createElement("span",{className:"nav-link"},t.nickname)),i.a.createElement("li",{className:"nav-item",onClick:this.logout.bind(this)},i.a.createElement("span",{className:"nav-link"},"\u767b\u51fa"))):i.a.createElement("ul",{className:"nav navbar-nav navbar-right"},i.a.createElement("li",{className:"nav-item",onClick:function(){return e.setState({loginVisiable:!0})}},i.a.createElement("span",{className:"nav-link"},"\u767b\u5f55")),i.a.createElement("li",{className:"nav-item"},i.a.createElement("span",{className:"nav-link"},"\u6ce8\u518c"))))),i.a.createElement(v,{loginVisiable:this.state.loginVisiable,loginClose:function(){return e.setState({loginVisiable:!1})},setUserInfo:this.setUserInfo.bind(this)}))}}]),a}(s.Component)}}]);
//# sourceMappingURL=12.8e5a1e1b.chunk.js.map