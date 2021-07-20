<%page args="questions, subquestions"/>
## <%def name="add_answer_row(option,question)">
##         <row>
##             <qid><![CDATA[${question.qid}]]></qid>
##             <code><![CDATA[${option.code}]]></code>
##             <answer><![CDATA[${option.value}]]></answer>
##             <sortorder><![CDATA[${option.order}]]></sortorder>
##             <assessment_value><![CDATA[0]]></assessment_value>
##             <language><![CDATA[fr]]></language>
##             <scale_id><![CDATA[0]]></scale_id>
##         </row>
## </%def>
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
    ##             <%include file="answer_row.mako" args="option=answer,question=question"/>
    ##                 ${add_answer_row(answer, question)}

            <row>
                <qid><![CDATA[${question.qid}]]></qid>
                <code><![CDATA[${answer.code}]]></code>
                <answer><![CDATA[${answer.value}]]></answer>
                <sortorder><![CDATA[${answer.order}]]></sortorder>
                <assessment_value><![CDATA[0]]></assessment_value>
                <language><![CDATA[fr]]></language>
                <scale_id><![CDATA[0]]></scale_id>
            </row>
                %endfor
            %endfor
        </rows>
    </answers>