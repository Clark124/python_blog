(this.webpackJsonpblog_front_new=this.webpackJsonpblog_front_new||[]).push([[11],{211:function(e,t,a){},221:function(e,t,a){"use strict";a.r(t),a.d(t,"default",(function(){return h}));var n=a(62),r=a(8),i=a(9),o=a(11),s=a(10),c=a(0),l=a.n(c),u=a(44),m=a(72),d=a(52),p=a(226),f=a(34),h=(a(211),function(e){Object(o.a)(c,e);var t=Object(s.a)(c);function c(){var e;return Object(r.a)(this,c),(e=t.call(this)).loadMore=function(){(document.documentElement.scrollTop||document.body.scrollTop)+(document.documentElement.clientHeight||document.body.clientHeight)===(document.documentElement.scrollHeight||document.body.scrollHeight)&&e.getMoreArticleList()},e.state={list:[],page:1,has_next:!1,isDataArrive:!0},e}return Object(i.a)(c,[{key:"componentDidMount",value:function(){var e=this.state.page;this.getArticleList(e,10),window.addEventListener("scroll",this.loadMore)}},{key:"componentWillUnmount",value:function(){window.removeEventListener("scroll",this.loadMore)}},{key:"getArticleList",value:function(e,t){var a=this,n=this.props.match.params.username;if(n){var r={page_num:e,page_size:t};Object(f.r)(r,n).then((function(e){if(200===e.code){var t=e.data.pageInfo,n=t.has_next,r=t.next_number;a.setState({list:e.data.topics,has_next:n,page:r})}else p.b.error(e.error)}))}}},{key:"getMoreArticleList",value:function(){var e=this,t=this.state,a=t.isDataArrive,r=t.has_next,i=t.page;if(a&&r&&1!==i){this.setState({isDataArrive:!1});var o={page_num:i,page_size:10},s=this.props.match.params.username;Object(f.r)(o,s).then((function(t){if(200===t.code){var a=t.data.pageInfo,r=a.has_next,i=a.next_number;e.setState({list:[].concat(Object(n.a)(e.state.list),Object(n.a)(t.data.topics)),has_next:r,page:i,isDataArrive:!0})}else p.b.error(t.error)}))}}},{key:"render",value:function(){var e=this,t=this.state.list;return l.a.createElement("div",null,l.a.createElement(u.a,this.props),l.a.createElement("img",{src:a(73),className:"figure-img img-fluid w-100",alt:""}),l.a.createElement("div",{className:"container"},l.a.createElement("div",{className:"public-header",style:{marginBottom:20}},l.a.createElement("span",{className:"header-name"},"\u6587\u7ae0\u5217\u8868"),l.a.createElement("span",null,"\u4e0d\u8981\u8f7b\u6613\u653e\u5f03\u3002\u5b66\u4e60\u6210\u957f\u7684\u8def\u4e0a\uff0c\u6211\u4eec\u957f\u8def\u6f2b\u6f2b\uff0c\u53ea\u56e0\u5b66\u65e0\u6b62\u5883\u3002 ")),l.a.createElement("div",{className:"row"},l.a.createElement("div",{className:"col-md-8"},t.map((function(t,a){return l.a.createElement(m.a,Object.assign({data:t,key:a},e.props))})),0===t.length?l.a.createElement("div",{className:"no-data"},"\u6682\u65e0\u6570\u636e"):null),l.a.createElement("div",{className:"col-md-4"},l.a.createElement(d.a,this.props)))))}}]),c}(c.Component))},62:function(e,t,a){"use strict";function n(e,t){(null==t||t>e.length)&&(t=e.length);for(var a=0,n=new Array(t);a<t;a++)n[a]=e[a];return n}function r(e){return function(e){if(Array.isArray(e))return n(e)}(e)||function(e){if("undefined"!==typeof Symbol&&Symbol.iterator in Object(e))return Array.from(e)}(e)||function(e,t){if(e){if("string"===typeof e)return n(e,t);var a=Object.prototype.toString.call(e).slice(8,-1);return"Object"===a&&e.constructor&&(a=e.constructor.name),"Map"===a||"Set"===a?Array.from(a):"Arguments"===a||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(a)?n(e,t):void 0}}(e)||function(){throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}a.d(t,"a",(function(){return r}))},73:function(e,t,a){e.exports=a.p+"static/media/page_bg1.ece80134.png"}}]);
//# sourceMappingURL=11.aa13241d.chunk.js.map