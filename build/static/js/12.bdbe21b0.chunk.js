(this.webpackJsonpblog_front_new=this.webpackJsonpblog_front_new||[]).push([[12],{185:function(e,t,a){},228:function(e,t,a){"use strict";a.r(t),a.d(t,"default",(function(){return E}));var n=a(62),i=a(8),r=a(9),s=a(11),c=a(10),o=a(0),l=a.n(o),u=a(44),m=(a(185),a(216)),d=a(55),p=a.n(d);var h=function(e){Object(s.a)(a,e);var t=Object(c.a)(a);function a(){return Object(i.a)(this,a),t.apply(this,arguments)}return Object(r.a)(a,[{key:"render",value:function(){var e=this,t=this.props.data;return l.a.createElement(m.a,{autoplay:!0},t.map((function(t,a){var n=t.images.map((function(e){return function(e){var t=document.createElement("div");return t.innerHTML=e,t.innerText||t.textContent}(e)}));return l.a.createElement("div",{className:"carousel-item",key:t.id,onClick:function(){return e.props.history.push("/articleDetail/".concat(t.username,"/").concat(t.id))}},l.a.createElement("div",{className:"carousel-title"},t.title),l.a.createElement("img",{src:n[0]?n[0]:p.a,alt:"",className:"figure-img img-fluid w-100"}))})))}}]),a}(o.Component),v=a(72),f=a(52),g=a(34),b=a(226),E=function(e){Object(s.a)(a,e);var t=Object(c.a)(a);function a(){var e;return Object(i.a)(this,a),(e=t.call(this)).state={list:[],carouselList:[],page:1,has_next:!1,isDataArrive:!0},e}return Object(r.a)(a,[{key:"componentDidMount",value:function(){var e=this.state.page;this.getArticleList(e,10),this.getTopicCarousel(),window.addEventListener("scroll",this.loadMore.bind(this))}},{key:"componentWillUnmount",value:function(){window.removeEventListener("scroll",this.loadMore.bind(this))}},{key:"loadMore",value:function(){(document.documentElement.scrollTop||document.body.scrollTop)+(document.documentElement.clientHeight||document.body.clientHeight)===(document.documentElement.scrollHeight||document.body.scrollHeight)&&(console.log("\u5230\u5e95\u90e8\u4e86"),this.getMoreArticleList())}},{key:"getArticleList",value:function(e,t){var a=this,n={page_num:e,page_size:t};Object(g.h)(n).then((function(e){if(200===e.code){var t=e.data.pageInfo,n=t.has_next,i=t.next_number;a.setState({list:e.data.topics,has_next:n,page:i})}else b.b.error(e.error)}))}},{key:"getMoreArticleList",value:function(){var e=this,t=this.state,a=t.isDataArrive,i=t.has_next,r=t.page;if(a&&i&&1!==r){this.setState({isDataArrive:!1});var s={page_num:r,page_size:10};Object(g.h)(s).then((function(t){if(200===t.code){var a=t.data.pageInfo,i=a.has_next,r=a.next_number;e.setState({list:[].concat(Object(n.a)(e.state.list),Object(n.a)(t.data.topics)),has_next:i,page:r,isDataArrive:!0})}else b.b.error(t.error)}))}}},{key:"getTopicCarousel",value:function(){var e=this;Object(g.q)().then((function(t){200===t.code&&e.setState({carouselList:t.data.topics})}))}},{key:"render",value:function(){var e=this,t=this.state,a=t.list,n=t.carouselList;return l.a.createElement("div",null,l.a.createElement(u.a,this.props),l.a.createElement("div",{className:"container",style:{marginTop:"30px"}},l.a.createElement("div",{className:"row"},l.a.createElement("div",{className:"col-md-8"},l.a.createElement(h,Object.assign({data:n},this.props)),l.a.createElement("div",{style:{marginTop:"30px"}},a.map((function(t,a){return l.a.createElement(v.a,Object.assign({data:t,key:a},e.props))})))),l.a.createElement("div",{className:"col-md-4"},l.a.createElement(f.a,this.props)))))}}]),a}(o.Component)}}]);
//# sourceMappingURL=12.bdbe21b0.chunk.js.map