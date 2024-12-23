import{r as o,j as e,c as d}from"./index-DuBDSCQ2.js";const N=()=>{var x,m;const g=window.matchMedia("(prefers-color-scheme: dark)").matches,[i,h]=o.useState(g),[c,b]=o.useState(null);o.useEffect(()=>{document.documentElement.classList.toggle("dark",i)},[i]);const u=()=>{h(s=>!s)},j=s=>{b(c===s?null:s)},l=(s,a)=>i?a:s,t=(s,a)=>i?a:s;return e.jsxs("main",{className:`
        container mx-auto px-4 py-8 space-y-12
        ${l("bg-white","bg-gray-900 text-gray-100")}
        transition-colors duration-300
      `,children:[e.jsx("div",{className:"flex justify-end mb-6",children:e.jsx("button",{onClick:u,className:`
            p-3 rounded-full text-2xl
            ${i?"bg-yellow-500 text-gray-900":"bg-gray-200 text-gray-800"}
            hover:scale-110 transition-transform
            shadow-md hover:shadow-lg
          `,children:e.jsx("i",{className:`fas ${i?"fa-sun":"fa-moon"}`})})}),e.jsxs("section",{className:"max-w-6xl mx-auto space-y-8",children:[d.sections.filter(s=>s.aboutProduct||s.content).map(s=>e.jsx("div",{className:`
          ${l("bg-white","bg-gray-800")}
          shadow-lg rounded-lg overflow-hidden 
          transition-all duration-300 
          hover:shadow-xl transform hover:-translate-y-2
          w-full
        `,children:e.jsxs("div",{className:"p-8",children:[e.jsx("h2",{className:`
            text-3xl font-bold 
            ${t("text-blue-600","text-blue-400")} 
            mb-6 border-b-2 border-blue-500 pb-4
          `,children:s.aboutProduct?"About Our Product":s.title}),s.aboutProduct?e.jsxs("div",{children:[e.jsx("p",{className:`
                ${t("text-gray-700","text-gray-300")}
                leading-relaxed text-lg mb-6
              `,children:s.aboutProduct.description}),e.jsxs("div",{className:"mb-6",children:[e.jsx("h3",{className:`
                  text-2xl font-semibold 
                  ${t("text-blue-500","text-blue-300")}
                  mb-4
                `,children:"Key Features"}),e.jsx("div",{className:"grid md:grid-cols-2 gap-4",children:s.aboutProduct.features.map((a,r)=>e.jsxs("div",{className:`
                        ${l("bg-gray-100","bg-gray-700")}
                        p-4 rounded-lg
                      `,children:[e.jsx("h4",{className:`
                        text-xl font-bold mb-2
                        ${t("text-blue-600","text-blue-400")}
                      `,children:a.title}),e.jsx("p",{className:`
                        ${t("text-gray-600","text-gray-300")}
                        text-md
                      `,children:a.description})]},r))})]}),e.jsxs("div",{className:"mb-6",children:[e.jsx("h3",{className:`
                  text-2xl font-semibold 
                  ${t("text-blue-500","text-blue-300")}
                  mb-4
                `,children:"Applications"}),e.jsx("ul",{className:`
                  list-disc list-inside
                  ${t("text-gray-700","text-gray-300")}
                `,children:s.aboutProduct.applications.map((a,r)=>e.jsx("li",{className:"mb-2",children:a},r))})]}),e.jsxs("div",{className:"mb-6",children:[e.jsx("h3",{className:`
                  text-2xl font-semibold 
                  ${t("text-blue-500","text-blue-300")}
                  mb-4
                `,children:"Benefits"}),e.jsx("ul",{className:`
                  list-disc list-inside
                  ${t("text-gray-700","text-gray-300")}
                `,children:s.aboutProduct.benefits.map((a,r)=>e.jsx("li",{className:"mb-2",children:a},r))})]}),e.jsx("div",{className:"italic p-4 border-l-4 border-blue-500",children:e.jsx("p",{className:`
                  ${t("text-gray-700","text-gray-300")}
                `,children:s.aboutProduct.mission})})]}):e.jsx("p",{className:`
              ${t("text-gray-700","text-gray-300")}
              leading-relaxed text-lg
            `,children:s.content})]})},s.id)),e.jsx("section",{className:"max-w-6xl mx-auto px-4 py-8",children:e.jsx("div",{className:`
        ${l("bg-white","bg-gray-800")}
        shadow-lg rounded-lg overflow-hidden 
        transition-all duration-300 
        hover:shadow-xl transform hover:-translate-y-2
        w-full
      `,children:e.jsxs("div",{className:"p-8",children:[e.jsx("h2",{className:`
          text-3xl font-bold 
          ${t("text-blue-600","text-blue-400")} 
          mb-6 border-b-2 border-blue-500 pb-4
        `,children:"Technology Used"}),e.jsx("p",{className:`
          ${t("text-gray-700","text-gray-300")}
          leading-relaxed text-lg mb-6
        `,children:"Our Fire Early Warning and Detection System leverages state-of-the-art technologies to provide unparalleled safety and precision. This solution integrates advancements in artificial intelligence, IoT, and hardware engineering to revolutionize fire safety systems."}),e.jsx("div",{className:"grid md:grid-cols-2 gap-6",children:d.sections.filter(s=>s.technologyUsed).flatMap(s=>{var a;return(a=s.technologyUsed)==null?void 0:a.technologies.map((r,n)=>e.jsxs("div",{className:`
                    ${l("bg-gray-100","bg-gray-700")}
                    p-6 rounded-lg shadow-md
                    transition-all duration-300
                    hover:scale-105
                  `,children:[e.jsx("h3",{className:`
                    text-2xl font-semibold mb-4
                    ${t("text-blue-600","text-blue-400")}
                  `,children:r.name}),e.jsx("ul",{className:`
                    list-disc list-inside
                    ${t("text-gray-700","text-gray-300")}
                    space-y-2
                  `,children:r.details.map((p,y)=>e.jsx("li",{className:"text-md",children:p},y))})]},n))})}),e.jsx("div",{className:"mt-8 p-6 border-l-4 border-blue-500 italic",children:e.jsx("p",{className:`
            ${t("text-gray-800","text-gray-200")}
            text-lg font-medium
          `,children:(m=(x=d.sections.find(s=>s.technologyUsed))==null?void 0:x.technologyUsed)==null?void 0:m.impact})})]})})}),e.jsxs("section",{id:"pros-cons",className:`
    ${l("bg-gray-50","bg-gray-800")} 
    rounded-lg shadow-md p-8
  `,children:[e.jsx("h2",{className:`
    text-3xl font-bold text-center 
    ${t("text-blue-600","text-blue-400")} 
    mb-8
  `,children:"Pros & Cons"}),e.jsxs("div",{className:"grid md:grid-cols-2 gap-8",children:[e.jsxs("div",{className:`
      ${l("bg-white","bg-gray-700")}
      rounded-lg shadow-md p-6
    `,children:[e.jsxs("h3",{className:`
        text-xl font-semibold text-green-600 mb-4 
        flex items-center
      `,children:[e.jsx("i",{className:"fas fa-check-circle mr-2"}),"Pros"]}),e.jsx("ul",{className:"space-y-4",children:Object.entries(d.pros[0]).map(([s,a])=>e.jsxs("li",{className:`
              flex items-start space-x-3 
              ${t("text-gray-800","text-gray-200")}
            `,children:[e.jsx("i",{className:"fas fa-check text-green-500 mt-1"}),e.jsxs("span",{children:[e.jsxs("strong",{className:"mr-2",children:[s,":"]}),a]})]},s))})]}),e.jsxs("div",{className:`
      ${l("bg-white","bg-gray-700")}
      rounded-lg shadow-md p-6
    `,children:[e.jsxs("h3",{className:`
        text-xl font-semibold text-red-600 mb-4 
        flex items-center
      `,children:[e.jsx("i",{className:"fas fa-times-circle mr-2"}),"Cons"]}),e.jsx("ul",{className:"space-y-4",children:Object.entries(d.cons[0]).map(([s,a])=>e.jsxs("li",{className:`
              flex items-start space-x-3 
              ${t("text-gray-800","text-gray-200")}
            `,children:[e.jsx("i",{className:"fas fa-times text-red-500 mt-1"}),e.jsxs("span",{children:[e.jsxs("strong",{className:"mr-2",children:[s,":"]}),a]})]},s))})]})]})]}),e.jsxs("section",{id:"faq",className:`
          ${l("bg-white","bg-gray-900")} 
          rounded-lg shadow-md p-8
        `,children:[e.jsx("h2",{className:`
          text-3xl font-bold text-center 
          ${t("text-blue-600","text-blue-400")} 
          mb-8
        `,children:"Frequently Asked Questions"}),e.jsx("div",{className:"space-y-6",children:d.faqs.map((s,a)=>e.jsxs("div",{children:[e.jsxs("h3",{className:`
                  text-xl font-semibold mb-4 cursor-pointer
                  ${t("text-gray-800","text-gray-200")}
                  flex justify-between items-center
                `,onClick:()=>j(s.category),children:[s.category,e.jsx("i",{className:`
                    fas 
                    ${c===s.category?"fa-chevron-up":"fa-chevron-down"}
                  `})]}),c===s.category&&e.jsx("div",{className:"space-y-4",children:s.questions.map((r,n)=>e.jsxs("div",{className:`
                        ${l("bg-gray-50","bg-gray-800")} 
                        rounded-lg p-6 mb-4 hover:bg-gray-100 transition duration-300
                      `,children:[e.jsx("h4",{className:`
                        text-lg font-medium 
                        ${t("text-blue-600","text-blue-400")} 
                        mb-2
                      `,children:r.question}),e.jsx("p",{className:`
                        ${t("text-gray-700","text-gray-300")}
                        leading-relaxed
                      `,children:r.answer})]},n))})]},a))})]})]}),e.jsxs("section",{id:"video",className:`
        ${l("bg-gray-50","bg-gray-800")} 
        rounded-lg p-8 text-center
      `,children:[e.jsx("h2",{className:`
          text-3xl font-bold 
          ${t("text-blue-600","text-blue-400")} 
          mb-8
        `,children:"Product Demo Video"}),e.jsx("div",{className:"max-w-4xl mx-auto bg-white rounded-lg shadow-lg overflow-hidden",children:e.jsxs("video",{controls:!0,className:"w-full",children:[e.jsx("source",{src:"../assets/demo.mp4",type:"video/mp4"}),"Your browser does not support the video tag."]})})]}),e.jsxs("section",{id:"gallery",className:`
        ${l("bg-gray-100","bg-gray-800")} 
        rounded-lg p-8
      `,children:[e.jsx("h2",{className:`
          text-3xl font-bold text-center 
          ${t("text-blue-600","text-blue-400")} 
          mb-8
        `,children:"Image Gallery"}),e.jsx("div",{className:"grid md:grid-cols-3 gap-6",children:["whatsapp.png","instagram.png","linkedin.png"].map((s,a)=>e.jsx("div",{className:`
                ${l("bg-white","bg-gray-700")}
                rounded-lg shadow-md overflow-hidden 
                transform transition duration-300 hover:scale-105
              `,children:e.jsx("img",{src:`../assets/${s}`,alt:`Slide ${a+1}`,className:"w-full h-64 object-cover"})},a))})]})]})},v=()=>e.jsx("div",{className:"container mx-auto p-4",children:e.jsx(N,{})});export{v as default};
