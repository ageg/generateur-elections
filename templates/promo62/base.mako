<?xml version="1.0" encoding="UTF-8"?>
<document>
   <LimeSurveyDocType>Survey</LimeSurveyDocType>
   <DBVersion>307</DBVersion>
   <languages>
      <language>fr</language>
   </languages>
   <%include file="answers.mako" args="questions=questions"/>
   <%include file="groups.mako" args="groups=groups"/>
   <%include file="questions.mako" args="questions=questions"/>
   <%include file="question_attributes.mako" args="questions=questions"/>
   <%include file="surveys.mako" />
   <%include file="surveys_languagesettings.mako" />
</document>