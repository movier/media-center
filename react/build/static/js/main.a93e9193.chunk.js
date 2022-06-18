(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{29:function(e,t,n){e.exports=n(43)},34:function(e,t,n){},39:function(e,t,n){},41:function(e,t,n){},42:function(e,t,n){},43:function(e,t,n){"use strict";n.r(t);var a=n(0),c=n.n(a),r=n(14),i=n.n(r),o=(n(34),n(7)),l=n(8),s=n(5),u=n(12),m=Object(u.b)({name:"video",initialState:{list:[]},reducers:{saveVideoListData:function(e,t){e.list=t.payload},removeVideo:function(e,t){e.list=e.list.filter(function(e){return e.id!==parseInt(t.payload)})}}}),d=m.actions,f=d.saveVideoListData,p=d.removeVideo,h=m.reducer,v=function(e){return e.video.list};n(39);var E=function(e){var t=e.media,n=t.uri,a=t.poster_uri,r=t.title,i=t.id,l=t.people,s=t.created_at,u=t.size,m=t.datetime,d=t.duration,f=l.map(function(e){return e.name}).join(",");return c.a.createElement("div",null,c.a.createElement(o.b,{className:"VideoList__link",to:"/watch?v=".concat(n,"&id=").concat(i,"&cast=").concat(f)},c.a.createElement("img",{src:a,alt:r}),c.a.createElement("p",{className:"VideoList__title"},r),c.a.createElement("p",{className:"VideoList__title"},s),c.a.createElement("p",{className:"VideoList__title"},function(e){var t=arguments.length>1&&void 0!==arguments[1]&&arguments[1],n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:1,a=t?1e3:1024;if(Math.abs(e)<a)return e+" B";var c=t?["kB","MB","GB","TB","PB","EB","ZB","YB"]:["KiB","MiB","GiB","TiB","PiB","EiB","ZiB","YiB"],r=-1,i=Math.pow(10,n);do{e/=a,++r}while(Math.round(Math.abs(e)*i)/i>=a&&r<c.length-1);return e.toFixed(n)+" "+c[r]}(u,!0)),c.a.createElement("p",{className:"VideoList__title"},m),c.a.createElement("p",{className:"VideoList__title"},new Date(1e3*Math.ceil(d)).toISOString().substr(11,8))))};function g(e){var t=Object(s.c)(v),n=Object(s.b)();Object(a.useEffect)(function(){t.length>0||fetch("/api").then(function(e){return e.json()}).then(function(t){if(console.log("response",t),t.has_error&&403===t.error_code){console.log("error",t.error_message);var a=t.data.remaining_seconds;e.history.replace("/remaining-time",{remainingSeconds:a})}else n(f(t))})},[]);return c.a.createElement("div",null,c.a.createElement("div",{style:{marginTop:16,textAlign:"center"}},c.a.createElement("button",{onClick:function(){fetch("/api?is_check=true").then(function(e){return e.json()}).then(function(e){n(f(e))})}},"\u68c0\u67e5\u66f4\u65b0"),c.a.createElement(o.b,{to:"/cast"},"Cast")),c.a.createElement("div",{className:"VideoList"},t.map(function(e,t){return c.a.createElement(E,{key:t,media:e})})))}var b=n(10),y=(n(41),Object(u.b)({name:"cast",initialState:{list:[]},reducers:{saveCastListData:function(e,t){e.list=t.payload},removeVideoFromPeople:function(e,t){for(var n=0;n<e.list.length;n++){var a=e.list[n];a.media=a.media.filter(function(e){return e.id!==parseInt(t.payload)})}}}})),j=y.actions,O=j.saveCastListData,S=j.removeVideoFromPeople,w=function(e){return e.cast.list},_=y.reducer;function B(e){var t=new URLSearchParams(e.location.search),n=t.get("id"),r=Object(a.useState)(t.get("cast").split(",")),i=Object(b.a)(r,2),o=i[0],l=i[1],u=Object(a.useState)(""),m=Object(b.a)(u,2),d=m[0],f=m[1],h=Object(a.useState)(""),v=Object(b.a)(h,2),E=v[0],g=v[1],y=Object(a.useState)(""),j=Object(b.a)(y,2),O=j[0],w=j[1],_=Object(a.useState)(null),B=Object(b.a)(_,2),k=B[0],C=B[1];Object(a.useEffect)(function(){fetch("/api/media/".concat(n)).then(function(e){return e.json()}).then(function(e){C(e)})},[]);var L=Object(s.b)();return k?c.a.createElement(c.a.Fragment,null,function(e){switch(e.media_type){case 1:return c.a.createElement("img",{src:e.uri});case 2:return c.a.createElement("video",{controls:!0,autoPlay:!0},c.a.createElement("source",{src:t.get("v")}));default:return c.a.createElement("h1",null,"Unknown Media Type")}}(k),c.a.createElement("button",{onClick:function(){window.confirm("Are you sure to delete this video?")&&fetch("/api/media/".concat(n),{method:"DELETE"}).then(function(){L(p(n)),L(S(n)),e.history.goBack()})}},"Delete"),c.a.createElement("div",null,o.map(function(e,t){return c.a.createElement("span",{style:{marginRight:10},key:t},e)})),c.a.createElement("div",null,c.a.createElement("span",null,"New Cast:"),c.a.createElement("input",{type:"text",value:d,onChange:function(e){return f(e.target.value)}}),c.a.createElement("button",{onClick:function(){if(d){var e={cast_name:d};fetch("/api/media/".concat(n),{method:"PUT",headers:{"Content-Type":"application/json"},body:JSON.stringify(e)}).then(function(){l(o.concat(d)),f("")})}}},"Add Cast")),c.a.createElement("div",null,c.a.createElement("span",null,"Start:"),c.a.createElement("input",{type:"text",value:E,onChange:function(e){return g(e.target.value)}}),c.a.createElement("span",null,"End:"),c.a.createElement("input",{type:"text",value:O,onChange:function(e){return w(e.target.value)}}),c.a.createElement("button",{onClick:function(){if(E&&O){var e=t.get("v"),n=e.split("."),a=Object(b.a)(n,2),c=a[0],r=a[1],i={input:e,output:"".concat(c,"_copy.").concat(r),start:E,end:O},o=document.getElementById("favicon");o.href="/loading.gif",fetch("/api/ffmpeg",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(i)}).then(function(){o.href="/favicon.ico"})}}},"Confirm"))):null}var k=n(25),C=n(26),L=n(16),M=n(28),T=n(27),V=function(e){Object(M.a)(n,e);var t=Object(T.a)(n);function n(e){var a;Object(k.a)(this,n),a=t.call(this,e),console.log("history state",e.location);var c=e.location.state.remainingSeconds;return a.state={remainingSeconds:c},a.secondsToString=a.secondsToString.bind(Object(L.a)(a)),a}return Object(C.a)(n,[{key:"componentDidMount",value:function(){var e=this,t=setInterval(function(){0===e.state.remainingSeconds?(clearInterval(t),e.props.history.replace("/")):e.setState({remainingSeconds:e.state.remainingSeconds-1})},1e3)}},{key:"secondsToString",value:function(e){return Math.floor(e/31536e3)+" years "+Math.floor(e%31536e3/86400)+" days "+Math.floor(e%31536e3%86400/3600)+" hours "+Math.floor(e%31536e3%86400%3600/60)+" minutes "+e%31536e3%86400%3600%60+" seconds"}},{key:"render",value:function(){return c.a.createElement("h1",{style:{color:"white"}},"Remaining time: ",this.secondsToString(this.state.remainingSeconds)," ")}}]),n}(c.a.Component);n(42);function N(){var e=Object(s.c)(w),t=Object(s.b)();return Object(a.useEffect)(function(){e.length>0||fetch("/api/cast").then(function(e){return e.json()}).then(function(e){t(O(e))})},[]),c.a.createElement("div",null,e.map(function(e,t){var n=e.name,a=e.media;return c.a.createElement("div",{key:t},c.a.createElement("div",{style:{color:"white"}},n),c.a.createElement("div",{className:"VideoList"},a.map(function(e,t){return c.a.createElement(E,{key:t,media:e})})))}))}function P(e){var t=e.match;return c.a.createElement("div",null,c.a.createElement("h2",null,"Topics"),c.a.createElement("ul",null,c.a.createElement("li",null,c.a.createElement(o.b,{to:"".concat(t.url,"/rendering")},"Rendering with React")),c.a.createElement("li",null,c.a.createElement(o.b,{to:"".concat(t.url,"/components")},"Components")),c.a.createElement("li",null,c.a.createElement(o.b,{to:"".concat(t.url,"/props-v-state")},"Props v. State"))),c.a.createElement(l.a,{path:"".concat(t.path,"/:topicId"),component:I}),c.a.createElement(l.a,{exact:!0,path:t.path,render:function(){return c.a.createElement("h3",null,"Please select a topic.")}}))}function I(e){var t=e.match;return c.a.createElement("div",null,c.a.createElement("h3",null,t.params.topicId))}var x=function(){return c.a.createElement(o.a,null,c.a.createElement("div",null,c.a.createElement(l.a,{exact:!0,path:"/",component:g}),c.a.createElement(l.a,{path:"/watch",component:B}),c.a.createElement(l.a,{path:"/topics",component:P}),c.a.createElement(l.a,{path:"/remaining-time",component:V}),c.a.createElement(l.a,{path:"/cast",component:N})))},D=Object(u.a)({reducer:{video:h,cast:_}});Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));i.a.render(c.a.createElement(c.a.StrictMode,null,c.a.createElement(s.a,{store:D},c.a.createElement(x,null))),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then(function(e){e.unregister()}).catch(function(e){console.error(e.message)})}},[[29,1,2]]]);
//# sourceMappingURL=main.a93e9193.chunk.js.map