<%page args="subquestions"/>
    <subquestions>
        <fields>
            <fieldname>qid</fieldname>
            <fieldname>parent_qid</fieldname>
            <fieldname>sid</fieldname>
            <fieldname>gid</fieldname>
            <fieldname>type</fieldname>
            <fieldname>title</fieldname>
            <fieldname>question</fieldname>
            <fieldname>preg</fieldname>
            <fieldname>help</fieldname>
            <fieldname>other</fieldname>
            <fieldname>mandatory</fieldname>
            <fieldname>question_order</fieldname>
            <fieldname>language</fieldname>
            <fieldname>scale_id</fieldname>
            <fieldname>same_default</fieldname>
            <fieldname>relevance</fieldname>
            <fieldname>modulename</fieldname>
        </fields>
        <rows>
        %for subquestion in subquestions:
    ##         <%include file="subquestion_row.mako" args="subquestion=subquestion"

            <row>
                <qid><![CDATA[${subquestion.qid}]]></qid>
                <parent_qid><![CDATA[${subquestion.parent}]]></parent_qid>
                <sid><![CDATA[172244]]></sid>
                <gid><![CDATA[${subquestion.gid}]]></gid>
                <type><![CDATA[${subquestion.type}]]></type>
                <title><![CDATA[${subquestion.code}]]></title>
                <question><![CDATA[${subquestion.value}]]></question>
                <other><![CDATA[N]]></other>
                <question_order><![CDATA[${subquestion.order}]]></question_order>
                <language><![CDATA[fr]]></language>
                <scale_id><![CDATA[0]]></scale_id>
                <same_default><![CDATA[0]]></same_default>
                <relevance><![CDATA[1]]></relevance>
                <modulename/>
            </row>
        %endfor
        </rows>
    </subquestions>