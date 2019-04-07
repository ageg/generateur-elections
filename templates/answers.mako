<%page args="questions, subquestions"/>
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
        %for answer in question.answers:
            <%include file="answer_row.mako" args="option=answer,question=question"/>
        %endfor
    %endfor
    </rows>
</answers>