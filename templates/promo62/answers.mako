<%page args="questions"/>
<answers>
    <fields>
        <fieldname>qid</fieldname>
        <fieldname>code</fieldname>
        <fieldname>answer</fieldname>
        <fieldname>sortorder</fieldname>
        <fieldname>assessment_value</fieldname>
        <fieldname>language</fieldname>
        <fieldname>scale_id</fieldname>
    </fields>

    <rows>
    %for question in questions:
        %for option in question.options:
            <%include file="answer_row.mako" args="option=option,question=question"/>
        %endfor
    %endfor
    </rows>
</answers>