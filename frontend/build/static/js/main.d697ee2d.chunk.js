(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{23:function(e,t,n){e.exports=n(35)},28:function(e,t,n){},29:function(e,t,n){},34:function(e,t,n){},35:function(e,t,n){"use strict";n.r(t);var a=n(0),c=n.n(a),o=n(20),r=n.n(o),l=(n(28),n(6)),i=n(5),u=n(9),s=n(10),m=n(12),h=n(11),p=n(13),d=(n(29),function(e){function t(e){var n;return Object(u.a)(this,t),(n=Object(m.a)(this,Object(h.a)(t).call(this,e))).handleCheckUpdate=function(){fetch("/api?is_check=true").then(function(e){return e.json()}).then(function(e){n.setState({data:e})})},n.state={data:[]},n}return Object(p.a)(t,e),Object(s.a)(t,[{key:"componentDidMount",value:function(){var e=this;fetch("/api").then(function(e){return e.json()}).then(function(t){console.log("response",t),e.setState({data:t})})}},{key:"render",value:function(){return c.a.createElement("div",null,c.a.createElement("div",{style:{marginTop:16,textAlign:"center"}},c.a.createElement("button",{onClick:this.handleCheckUpdate},"\u68c0\u67e5\u66f4\u65b0")),c.a.createElement("div",{className:"VideoList"},this.state.data.map(function(e,t){return c.a.createElement("div",{key:t},c.a.createElement(l.b,{className:"VideoList__link",to:"/watch?v=".concat(e.uri)},c.a.createElement("img",{src:e.poster_uri,alt:e.title}),c.a.createElement("p",{className:"VideoList__title"},e.title)))})))}}]),t}(c.a.Component)),E=(n(34),function(e){function t(e){var n;Object(u.a)(this,t),n=Object(m.a)(this,Object(h.a)(t).call(this,e)),console.log("dd",e.location.search);var a=new URLSearchParams(e.location.search);return console.log("video detail",a.get("v")),n}return Object(p.a)(t,e),Object(s.a)(t,[{key:"render",value:function(){var e=new URLSearchParams(this.props.location.search);return c.a.createElement(c.a.Fragment,null,c.a.createElement("video",{controls:!0,autoPlay:!0},c.a.createElement("source",{src:e.get("v")})))}}]),t}(c.a.Component));function v(e){var t=e.match;return c.a.createElement("div",null,c.a.createElement("h2",null,"Topics"),c.a.createElement("ul",null,c.a.createElement("li",null,c.a.createElement(l.b,{to:"".concat(t.url,"/rendering")},"Rendering with React")),c.a.createElement("li",null,c.a.createElement(l.b,{to:"".concat(t.url,"/components")},"Components")),c.a.createElement("li",null,c.a.createElement(l.b,{to:"".concat(t.url,"/props-v-state")},"Props v. State"))),c.a.createElement(i.a,{path:"".concat(t.path,"/:topicId"),component:f}),c.a.createElement(i.a,{exact:!0,path:t.path,render:function(){return c.a.createElement("h3",null,"Please select a topic.")}}))}function f(e){var t=e.match;return c.a.createElement("div",null,c.a.createElement("h3",null,t.params.topicId))}var b=function(){return c.a.createElement(l.a,null,c.a.createElement("div",null,c.a.createElement(i.a,{exact:!0,path:"/",component:d}),c.a.createElement(i.a,{path:"/watch",component:E}),c.a.createElement(i.a,{path:"/topics",component:v})))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));r.a.render(c.a.createElement(b,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then(function(e){e.unregister()})}},[[23,1,2]]]);
//# sourceMappingURL=main.d697ee2d.chunk.js.map