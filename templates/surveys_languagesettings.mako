 <%page args="survey_options"/><surveys_languagesettings>
  <fields>
   <fieldname>surveyls_survey_id</fieldname>
   <fieldname>surveyls_language</fieldname>
   <fieldname>surveyls_title</fieldname>
   <fieldname>surveyls_description</fieldname>
   <fieldname>surveyls_welcometext</fieldname>
   <fieldname>surveyls_endtext</fieldname>
   <fieldname>surveyls_url</fieldname>
   <fieldname>surveyls_urldescription</fieldname>
   <fieldname>surveyls_email_invite_subj</fieldname>
   <fieldname>surveyls_email_invite</fieldname>
   <fieldname>surveyls_email_remind_subj</fieldname>
   <fieldname>surveyls_email_remind</fieldname>
   <fieldname>surveyls_email_register_subj</fieldname>
   <fieldname>surveyls_email_register</fieldname>
   <fieldname>surveyls_email_confirm_subj</fieldname>
   <fieldname>surveyls_email_confirm</fieldname>
   <fieldname>surveyls_dateformat</fieldname>
   <fieldname>surveyls_attributecaptions</fieldname>
   <fieldname>email_admin_notification_subj</fieldname>
   <fieldname>email_admin_notification</fieldname>
   <fieldname>email_admin_responses_subj</fieldname>
   <fieldname>email_admin_responses</fieldname>
   <fieldname>surveyls_numberformat</fieldname>
   <fieldname>attachments</fieldname>
  </fields>
  <rows>
   <row>
    <surveyls_survey_id><![CDATA[172244]]></surveyls_survey_id>
    <surveyls_language><![CDATA[fr]]></surveyls_language>
    <surveyls_title><![CDATA[${survey_options.title}]]></surveyls_title>
    <surveyls_description><![CDATA[${survey_options.description}]]></surveyls_description>
    <surveyls_welcometext><![CDATA[${survey_options.welcome_text}]]></surveyls_welcometext>
    <surveyls_endtext><![CDATA[${survey_options.end_text}]]></surveyls_endtext>
    <surveyls_url><![CDATA[https://www.ageg.ca]]></surveyls_url>
    <surveyls_urldescription/>
    <surveyls_email_invite_subj><![CDATA[${survey_options.email_invite_subject}]]></surveyls_email_invite_subj>
    <surveyls_email_invite><![CDATA[${survey_options.email_invite_body}]]></surveyls_email_invite>
    <surveyls_email_remind_subj><![CDATA[${survey_options.email_reminder_subject}]]></surveyls_email_remind_subj>
    <surveyls_email_remind><![CDATA[${survey_options.email_reminder_body}]]></surveyls_email_remind>
    <surveyls_email_register_subj><![CDATA[Confirmation d'enregistrement au questionnaire]]></surveyls_email_register_subj>
    <surveyls_email_register><![CDATA[<html>
<head>
	<title></title>
</head>
<body>Bonjour {FIRSTNAME},<br />
<br />
Vous (ou quelqu’un utilisant votre adresse électronique) vous êtes enregistré pour participer à un questionnaire en ligne intitulé {SURVEYNAME}.<br />
<br />
Pour compléter ce questionnaire, cliquez sur le lien suivant :<br />
{SURVEYURL}<br />
<br />
Si vous avez des questions à propos de ce questionnaire, ou si vous ne vous êtes pas enregistré pour participer à celui-ci et croyez que ce courriel est une erreur, veuillez contacter {ADMINNAME} à l’adresse {ADMINEMAIL}</body>
</html>
]]></surveyls_email_register>
    <surveyls_email_confirm_subj><![CDATA[Confirmation de votre participation à notre questionnaire]]></surveyls_email_confirm_subj>
    <surveyls_email_confirm><![CDATA[<html>
<head>
	<title></title>
</head>
<body>Bonjour {FIRSTNAME},<br />
<br />
Ce courriel vous confirme que votre réponse a été enregistrée. Merci pour votre participation.<br />
<br />
Si vous avez des questions à propos de ce courriel, veuillez contacter {ADMINNAME} à l’adresse {ADMINEMAIL}.<br />
<br />
Merci,<br />
{ADMINNAME}</body>
</html>
]]></surveyls_email_confirm>
    <surveyls_dateformat><![CDATA[2]]></surveyls_dateformat>
    <email_admin_notification_subj><![CDATA[Soumission de réponse pour le questionnaire {SURVEYNAME}]]></email_admin_notification_subj>
    <email_admin_notification><![CDATA[<html>
<head>
	<title></title>
</head>
<body>Bonjour,<br />
<br />
Une nouvelle réponse a été soumise pour votre questionnaire '{SURVEYNAME}'.<br />
<br />
Cliquez sur le lien suivant pour recharger votre questionnaire :<br />
{RELOADURL}<br />
<br />
Cliquez sur le lien suivant pour voir la réponse :<br />
{VIEWRESPONSEURL}<br />
<br />
Cliquez sur le lien suivant pour éditer la réponse :<br />
{EDITRESPONSEURL}<br />
<br />
Visualisez les statistiques en cliquant ici :<br />
{STATISTICSURL}<br />
<br />
les réponses suivantes ont été données par le participant :<br />
{ANSWERTABLE}</body>
</html>
]]></email_admin_notification>
    <email_admin_responses_subj><![CDATA[Soumission de réponse pour le questionnaire {SURVEYNAME} avec résultats]]></email_admin_responses_subj>
    <email_admin_responses><![CDATA[<html>
<head>
	<title></title>
</head>
<body>Bonjour,<br />
<br />
Une nouvelle réponse a été soumise pour votre questionnaire '{SURVEYNAME}'.<br />
<br />
Cliquez sur le lien suivant pour recharger votre questionnaire :<br />
{RELOADURL}<br />
<br />
Cliquez sur le lien suivant pour voir la réponse :<br />
{VIEWRESPONSEURL}<br />
<br />
Cliquez sur le lien suivant pour éditer la réponse individuelle :<br />
{EDITRESPONSEURL}<br />
<br />
Visualisez les statistiques en cliquant ici :<br />
{STATISTICSURL}<br />
<br />
<br />
les réponses suivantes ont été données par le participant :<br />
{ANSWERTABLE}</body>
</html>
]]></email_admin_responses>
    <surveyls_numberformat><![CDATA[1]]></surveyls_numberformat>
    <attachments><![CDATA[a:0:{}]]></attachments>
   </row>
  </rows>
 </surveys_languagesettings>