<%page args="questions"/>
<question_attributes>
    <fields>
        <fieldname>qid</fieldname>
        <fieldname>attribute</fieldname>
        <fieldname>value</fieldname>
        <fieldname>language</fieldname>
    </fields>
    <rows>
    %for question in questions:
##         <%include file="question_attribute_row.mako" args="question=question"/>
        %for attribute in question.attributes:
        <row>
            <qid><![CDATA[${question.qid}]]></qid>
            <attribute><![CDATA[${attribute.name}]]></attribute>
            <value><![CDATA[${attribute.value}]]></value>
        </row>
        %endfor
    %endfor    
    </rows>
</question_attributes>