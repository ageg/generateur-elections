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
##             <%include file="question_row.mako" args="question=question"/>

            <row>
                <qid><![CDATA[${question.qid}]]></qid>
                <parent_qid><![CDATA[0]]></parent_qid>
                <sid><![CDATA[544188]]></sid>
                <gid><![CDATA[${question.gid}]]></gid>
                <type><![CDATA[${question.type}]]></type>
                <title><![CDATA[${question.code}]]></title>
                <question><![CDATA[
##                     <%include file="question_description.mako" args="title=question.title, options=question.options"/>
<p>${question.title}</p>

<table border="1" cellpadding="0" cellspacing="1">
    <tbody>
        %for option in question.options:
        <tr style="border-bottom: 1px solid white;">
            <td>
                %if option.concentration and option.promotion:
                <p><strong>${option.value} (${option.concentration}, ${option.promotion})</strong></p>
                %elif option.concentration:
                <p><strong>${option.value} (${option.concentration})</strong></p>
                %else:
                <p><strong>${option.value}</strong></p>
                %endif
                %for line in option.description.split('\n'):
                <p>${line}</p>
                %endfor
            </td>
            <td>
                <p>
                    <img src="${option.image}" width="300" alt="${option.value}" />
                </p>
            </td>
        </tr>
        %endfor
    </tbody>
</table>
                ]]></question>
                <preg/>
                <help><![CDATA[${question.help}]]></help>
                <other><![CDATA[N]]></other>
                <mandatory><![CDATA[N]]></mandatory>
                <question_order><![CDATA[${question.order}]]></question_order>
                <language><![CDATA[fr]]></language>
                <scale_id><![CDATA[0]]></scale_id>
                <same_default><![CDATA[0]]></same_default>
                <relevance><![CDATA[1]]></relevance>
                <modulename/>
            </row>
        %endfor
        </rows>
    </questions>