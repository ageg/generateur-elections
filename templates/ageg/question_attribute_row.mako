<%page args="question"/>
%for attribute in question.attributes:
<row>
    <qid><![CDATA[${question.qid}]]></qid>
    <attribute><![CDATA[${attribute.name}]]></attribute>
    <value><![CDATA[${attribute.value}]]></value>
</row>
%endfor 

