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
        <%include file="question_attribute_row.mako" args="question=question"/>
    %endfor    
    </rows>
</question_attributes>