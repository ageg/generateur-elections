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
        <%include file="subquestion_row.mako" args="subquestion=subquestion"/>
    %endfor
    </rows>
</subquestions>