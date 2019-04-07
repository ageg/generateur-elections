<%page args="question"/>
<row>
    <qid><![CDATA[${question.qid}]]></qid>
    <parent_qid><![CDATA[0]]></parent_qid>
    <sid><![CDATA[544188]]></sid>
    <gid><![CDATA[${question.gid}]]></gid>
    <type><![CDATA[${question.type}]]></type>
    <title><![CDATA[${question.code}]]></title>
    <question><![CDATA[
        <%include file="question_description.mako" args="title=question.title, options=question.options"/>
    ]]></question>
    <preg/>
    <help><![CDATA[Pour ce poste, une seule personne peut-être élue. Veuillez placer les candidatures en ordre de préférence, du haut vers le bas.]]></help>
    <other><![CDATA[N]]></other>
    <mandatory><![CDATA[N]]></mandatory>
    <question_order><![CDATA[${question.order}]]></question_order>
    <language><![CDATA[fr]]></language>
    <scale_id><![CDATA[0]]></scale_id>
    <same_default><![CDATA[0]]></same_default>
    <relevance><![CDATA[1]]></relevance>
    <modulename/>
</row>