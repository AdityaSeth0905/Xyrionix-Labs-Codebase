import React from 'react';
import privacyPolicy from '../components/privacyPolicyContent.json'; // Path to your JSON file
import "./privacyPolicy.css"; // Path to your CSS file


interface SectionContent {
  heading?: string;
  items?: string[];
  [key: string]: any; // For fallback in case of unexpected JSON structure
}

interface Section {
  id: string;
  title: string;
  content: SectionContent[];
}

interface PrivacyPolicyData {
  title: string;
  sections: Section[];
}

function PrivacyPolicy() {
  const policyData = privacyPolicy as PrivacyPolicyData;

  return (
    <div className="privacy-policy">
      <h1>{policyData.title}</h1>
      {policyData.sections.map((section) => (
        <section id={section.id} key={section.id}>
          <h2>{section.title}</h2>
          {section.content.map((content, index) => (
            <div key={index}>
              {content.heading && <h3>{content.heading}</h3>}
              {content.items && Array.isArray(content.items) && (
                <ul>
                  {content.items.map((item, i) => (
                    <li key={i}>{item}</li>
                  ))}
                </ul>
              )}
              {typeof content === 'string' && <p>{content}</p>}
            </div>
          ))}
        </section>
      ))}
    </div>
  );
}

export default PrivacyPolicy;