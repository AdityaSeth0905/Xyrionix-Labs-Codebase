import React, { useState } from 'react';
import '@fortawesome/fontawesome-free/css/all.min.css';
import content from './content.json';

const MainContent: React.FC = () => {
  const [activeSection, setActiveSection] = useState<string | null>(null);
  const [isDarkTheme, setIsDarkTheme] = useState(false);
  const [activeCategory, setActiveCategory] = useState<string | null>(null);

  const toggleTheme = () => {
    setIsDarkTheme(!isDarkTheme);
    document.documentElement.classList.toggle('dark');
  };

  const toggleSection = (sectionId: string) => {
    setActiveSection(activeSection === sectionId ? null : sectionId);
  };

  const toggleFAQCategory = (category: string) => {
    setActiveCategory(activeCategory === category ? null : category);
  };

  // Dynamic background and text color classes
  const bgClass = (lightClass: string, darkClass: string) => 
    isDarkTheme ? darkClass : lightClass;

  // Dynamic text color classes
  const textClass = (lightClass: string, darkClass: string) => 
    isDarkTheme ? darkClass : lightClass;

  return (
    <main 
      className={`
        container mx-auto px-4 py-8 space-y-12
        ${bgClass('bg-white', 'bg-gray-900 text-gray-100')}
        transition-colors duration-300
      `}
    >
      {/* Theme Toggle Button */}
      <div className="flex justify-end mb-6">
        <button 
          onClick={toggleTheme}
          className={`
            p-3 rounded-full text-2xl
            ${isDarkTheme 
              ? 'bg-yellow-500 text-gray-900' 
              : 'bg-gray-200 text-gray-800'}
            hover:scale-110 transition-transform
            shadow-md hover:shadow-lg
          `}
        >
          <i className={`fas ${isDarkTheme ? 'fa-sun' : 'fa-moon'}`}></i>
        </button>
      </div>

{/* Sections Container */}
<section className="max-w-6xl mx-auto space-y-8">
  {content.sections.map((section) => (
    <div 
      key={section.id} 
      className={`
        ${bgClass('bg-white', 'bg-gray-800')}
        shadow-lg rounded-lg overflow-hidden 
        transition-all duration-300 
        hover:shadow-xl transform hover:-translate-y-2
        w-full
      `}
    >
      <div className="p-8">
        <h2 className={`
          text-3xl font-bold 
          ${textClass('text-blue-600', 'text-blue-400')} 
          mb-6 border-b-2 border-blue-500 pb-4
        `}>
          {section.aboutProduct ? "About Our Product" : section.title}
        </h2>
        
        {/* Conditional rendering for About Product */}
        {section.aboutProduct ? (
          <div>
            <p className={`
              ${textClass('text-gray-700', 'text-gray-300')}
              leading-relaxed text-lg mb-6
            `}>
              {section.aboutProduct.description}
            </p>

            {/* Features Section */}
            <div className="mb-6">
              <h3 className={`
                text-2xl font-semibold 
                ${textClass('text-blue-500', 'text-blue-300')}
                mb-4
              `}>
                Key Features
              </h3>
              <div className="grid md:grid-cols-2 gap-4">
                {section.aboutProduct.features.map((feature, index) => (
                  <div 
                    key={index} 
                    className={`
                      ${bgClass('bg-gray-100', 'bg-gray-700')}
                      p-4 rounded-lg
                    `}
                  >
                    <h4 className={`
                      text-xl font-bold mb-2
                      ${textClass('text-blue-600', 'text-blue-400')}
                    `}>
                      {feature.title}
                    </h4>
                    <p className={`
                      ${textClass('text-gray-600', 'text-gray-300')}
                      text-md
                    `}>
                      {feature.description}
                    </p>
                  </div>
                ))}
              </div>
            </div>

            {/* Applications Section */}
            <div className="mb-6">
              <h3 className={`
                text-2xl font-semibold 
                ${textClass('text-blue-500', 'text-blue-300')}
                mb-4
              `}>
                Applications
              </h3>
              <ul className={`
                list-disc list-inside
                ${textClass('text-gray-700', 'text-gray-300')}
              `}>
                {section.aboutProduct.applications.map((app, index) => (
                  <li key={index} className="mb-2">{app}</li>
                ))}
              </ul>
            </div>

            {/* Benefits Section */}
            <div className="mb-6">
              <h3 className={`
                text-2xl font-semibold 
                ${textClass('text-blue-500', 'text-blue-300')}
                mb-4
              `}>
                Benefits
              </h3>
              <ul className={`
                list-disc list-inside
                ${textClass('text-gray-700', 'text-gray-300')}
              `}>
                {section.aboutProduct.benefits.map((benefit, index) => (
                  <li key={index} className="mb-2">{benefit}</li>
                ))}
              </ul>
            </div>

            {/* Mission Statement */}
            <div className="italic p-4 border-l-4 border-blue-500">
              <p className={`
                ${textClass('text-gray-700', 'text-gray-300')}
              `}>
                {section.aboutProduct.mission}
              </p>
            </div>
          </div>
        ) : 
        (
          <p className={`
            ${textClass('text-gray-700', 'text-gray-300')}
            leading-relaxed text-lg
          `}>
            {section.content}
          </p>
        )}
      </div>
    </div>
  ))}

  {/* Technology Used Section */}
  <section className="max-w-6xl mx-auto px-4 py-8">
    <div 
      className={`
        ${bgClass('bg-white', 'bg-gray-800')}
        shadow-lg rounded-lg overflow-hidden 
        transition-all duration-300 
        hover:shadow-xl transform hover:-translate-y-2
        w-full
      `}
    >
      <div className="p-8">
        {/* Section Heading */}
        <h2 className={`
          text-3xl font-bold 
          ${textClass('text-blue-600', 'text-blue-400')} 
          mb-6 border-b-2 border-blue-500 pb-4
        `}>
          Technology Used
        </h2>

        {/* Description */}
        <p className={`
          ${textClass('text-gray-700', 'text-gray-300')}
          leading-relaxed text-lg mb-6
        `}>
          Our Fire Early Warning and Detection System leverages state-of-the-art technologies to provide unparalleled safety and precision. This solution integrates advancements in artificial intelligence, IoT, and hardware engineering to revolutionize fire safety systems.
        </p>

        {/* Technologies Grid */}
        <div className="grid md:grid-cols-2 gap-6">
          {content.sections
            .filter(section => section.technologyUsed)
            .flatMap(section => 
              section.technologyUsed?.technologies.map((tech, index) => (
                <div 
                  key={index} 
                  className={`
                    ${bgClass('bg-gray-100', 'bg-gray-700')}
                    p-6 rounded-lg shadow-md
                    transition-all duration-300
                    hover:scale-105
                  `}
                >
                  <h3 className={`
                    text-2xl font-semibold mb-4
                    ${textClass('text-blue-600', 'text-blue-400')}
                  `}>
                    {tech.name}
                  </h3>
                  <ul className={`
                    list-disc list-inside
                    ${textClass('text-gray-700', 'text-gray-300')}
                    space-y-2
                  `}>
                    {tech.details.map((detail, detailIndex) => (
                      <li key={detailIndex} className="text-md">
                        {detail}
                      </li>
                    ))}
                  </ul>
                </div>
              ))
            )}
        </div>

        {/* Impact Statement */}
        <div className="mt-8 p-6 border-l-4 border-blue-500 italic">
          <p className={`
            ${textClass('text-gray-800', 'text-gray-200')}
            text-lg font-medium
          `}>
            {content.sections
              .find(section => section.technologyUsed)
              ?.technologyUsed?.impact}
          </p>
        </div>  
      </div>
    </div>
  </section>
</section>
        

      {/* Pros & Cons Section */}
      <section 
        id="pros-cons" 
        className={`
          ${bgClass('bg-gray-50', 'bg-gray-800')} 
          rounded-lg shadow-md p-8
        `}
      >
        <h2 className={`
          text-3xl font-bold text-center 
          ${textClass('text-blue-600', 'text-blue-400')} 
          mb-8
        `}>
          Pros & Cons
        </h2>
        <div className="grid md:grid-cols-2 gap-8">
          {/* Pros Column */}
          <div className={`
            ${bgClass('bg-white', 'bg-gray-700')}
            rounded-lg shadow-md p-6
          `}>
            <h3 className={`
              text-xl font-semibold text-green-600 mb-4 
              flex items-center
            `}>
              <i className="fas fa-check-circle mr-2"></i>Pros
            </h3>
            <ul className="space-y-4">
              {content.pros.map((pro, index) => (
                <li 
                  key={index} 
                  className={`
                    flex items-start space-x-3 
                    ${textClass('text-gray-800', 'text-gray-200')}
                  `}
                >
                  <i className="fas fa-check text-green-500 mt-1"></i>
                  <span>{Object.values(pro)[0]}</span>
                </li>
              ))}
            </ul>
          </div>

          {/* Cons Column */}
          <div className={`
            ${bgClass('bg-white', 'bg-gray-700')}
            rounded-lg shadow-md p-6
          `}>
            <h3 className={`
              text-xl font-semibold text-red-600 mb-4 
              flex items-center
            `}>
              <i className="fas fa-times-circle mr-2"></i>Cons
            </h3>
            <ul className="space-y-4">
              {content.cons.map((con, index) => (
                <li 
                  key={index} 
                  className={`
                    flex items-start space-x-3 
                    ${textClass('text-gray-800', 'text-gray-200')}
                  `}
                >
                  <i className="fas fa-times text-red-500 mt-1"></i>
                  <span>{Object.values(con)[0]}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </section>

      {/* FAQ Section */}
      <section 
        id="faq" 
        className={`
          ${bgClass('bg-white', 'bg-gray-900')} 
          rounded-lg shadow-md p-8
        `}
      >
        <h2 className={`
          text-3xl font-bold text-center 
          ${textClass('text-blue-600', 'text-blue-400')} 
          mb-8
        `}>
          Frequently Asked Questions
        </h2>
        <div className="space-y-6">
          {content.faqs.map((faqCategory, categoryIndex) => (
            <div key={categoryIndex}>
              <h3 
                className={`
                  text-xl font-semibold mb-4 cursor-pointer
                  ${textClass('text-gray-800', 'text-gray-200')}
                  flex justify-between items-center
                `}
                onClick={() => toggleFAQCategory(faqCategory.category)}
              >
                {faqCategory.category}
                <i 
                  className={`
                    fas 
                    ${activeCategory === faqCategory.category 
                      ? 'fa-chevron-up' 
                      : 'fa-chevron-down'
                    }
                  `}
                ></i>
              </h3>
              {activeCategory === faqCategory.category && (
                <div className="space-y-4">
                  {faqCategory.questions.map((faq, questionIndex) => (
                    <div 
                      key={questionIndex}  className={`
                        ${bgClass('bg-gray-50', 'bg-gray-800')} 
                        rounded-lg p-6 mb-4 hover:bg-gray-100 transition duration-300
                      `}
                    >
                      <h4 className={`
                        text-lg font-medium 
                        ${textClass('text-blue-600', 'text-blue-400')} 
                        mb-2
                      `}>
                        {faq.question}
                      </h4>
                      <p className={`
                        ${textClass('text-gray-700', 'text-gray-300')}
                        leading-relaxed
                      `}>
                        {faq.answer}
                      </p>
                    </div>
                  ))}
                </div>
              )}
            </div>
          ))}
        </div>
      </section>

      {/* Video Section */}
      <section id="video" className={`
        ${bgClass('bg-gray-50', 'bg-gray-800')} 
        rounded-lg p-8 text-center
      `}>
        <h2 className={`
          text-3xl font-bold 
          ${textClass('text-blue-600', 'text-blue-400')} 
          mb-8
        `}>
          Product Demo Video
        </h2>
        <div className="max-w-4xl mx-auto bg-white rounded-lg shadow-lg overflow-hidden">
          <video 
            controls 
            className="w-full"
          >
            <source src="../assets/demo.mp4" type="video/mp4" />
            Your browser does not support the video tag.
          </video>
        </div>
      </section>

      {/* Image Gallery */}
      <section id="gallery" className={`
        ${bgClass('bg-gray-100', 'bg-gray-800')} 
        rounded-lg p-8
      `}>
        <h2 className={`
          text-3xl font-bold text-center 
          ${textClass('text-blue-600', 'text-blue-400')} 
          mb-8
        `}>
          Image Gallery
        </h2>
        <div className="grid md:grid-cols-3 gap-6">
          {['whatsapp.png', 'instagram.png', 'linkedin.png'].map((img, index) => (
            <div 
              key={index} 
              className={`
                ${bgClass('bg-white', 'bg-gray-700')}
                rounded-lg shadow-md overflow-hidden 
                transform transition duration-300 hover:scale-105
              `}
            >
              <img 
                src={`../assets/${img}`} 
                alt={`Slide ${index + 1}`} 
                className="w-full h-64 object-cover"
              />
            </div>
          ))}
        </div>
      </section>
    </main>
  );
};

export default MainContent;