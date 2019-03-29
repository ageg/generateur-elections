<%page args="questions"/>
<questions>
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
    %for question in questions:
        <%include file="question_row.mako" args="question=question"/>
    %endfor
    </rows>
</questions>