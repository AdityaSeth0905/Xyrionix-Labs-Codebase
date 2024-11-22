import React from 'react';
import { useState } from 'react';
import './App.css';
import Chatbot from './Chatbot';
import content from '../src/components/content.json';
import "./assets/instagram.png"
import PrivacyPolicy from './components/privacyPolicy';
function App() {
  return (
    <div>
      <header>
        <h1>{content.footer.companyName}</h1>
        <nav>
          {content.navBar[0] && 
            Object.entries(content.navBar[0]).map(([key, value]) => (
              <button
                key={key} // Use the key as a unique identifier
                onClick={() => window.location.hash = `#${key}`} // Use button key as hash ID
              >
                {value} {/* Display the button name */}
              </button>
          ))}
        </nav>
      </header>

      <main>
        {content.sections.map((section) => (
          <section id={section.id} key={section.id}>
            <h1>{section.title}</h1>
            <p>{section.content}</p>
          </section>
        ))}

        {/* Pros and Cons Section */}
        <section id="pros-cons">
          <h1>Pros & Cons</h1>
          <div className="pros-cons-container">
            <div className="pros">
              <h2>Pros</h2>
              <ul>
                {content.pros.map((pro, index) =>
                  Object.entries(pro).map(([key, value]) => (
                    <li key={`${key}-${index}`}>
                      <strong>{key}:</strong> {value}
                    </li>
                  ))
                )}
              </ul>
            </div>
            <div className="cons">
              <h2>Cons</h2>
              <ul>
                {content.cons.map((con, index) =>
                  Object.entries(con).map(([key, value]) => (
                    <li key={`${key}-${index}`}>
                      <strong>{key}:</strong> {value}
                    </li>
                  ))
                )}
              </ul>
            </div>
          </div>
        </section>
        {/* FAQs Section */}
        <section id="faqs">
          <h1>Frequently Asked Questions (FAQs)</h1>
          <div className="faq-section">
            {content.faqs.map((faqCategory, index) => (
              <div key={index}>
                <h2>{faqCategory.category}</h2>
                {faqCategory.questions.map((faq, qIndex) => (
                  <div key={qIndex} className="faq-item">
                    <h3>Q{qIndex + 1}: {faq.question}</h3>
                    <p>A{qIndex + 1}: {faq.answer}</p>
                  </div>
                ))}
              </div>
            ))}
          </div>
        </section>
      </main>

      <footer>
      <h2>{content.footer.companyName}</h2>
      <p><em>{content.footer.slogan}</em></p>
      <p>
        Contact us at: <a href={`mailto:${content.footer.contactEmail}`}>{content.footer.contactEmail}</a>
      </p>
      <div className="social-media">
        {content.footer.socialMedia.map((social, index) => (
          <a 
            key={index} 
            href={social.url} 
            target="_blank" 
            rel="noopener noreferrer"
            className="social-media-link"
          >
            <img 
              src={social.logo} 
              alt={`${social.platform} logo`} 
              className="social-media-logo" 
            />
            <span>{social.platform}</span>
          </a>
        ))}
      </div>
      <button id='privacyPolicy' onClick={PrivacyPolicy}>Privacy Policy</button>
    </footer>
      {/* Chatbot Instance */}
      <Chatbot />
    </div>
  )
}

export default App
