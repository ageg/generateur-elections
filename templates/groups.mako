<%page args="groups"/>
    <groups>
        <fields>
            <fieldname>gid</fieldname>
            <fieldname>sid</fieldname>
            <fieldname>group_name</fieldname>
            <fieldname>group_order</fieldname>
            <fieldname>description</fieldname>
            <fieldname>language</fieldname>
            <fieldname>randomization_group</fieldname>
            <fieldname>grelevance</fieldname>
        </fields>
        <rows>
        %for group in groups:
    ##         <%include file="group_row.mako" args="group=group"/>

            <row>
                <gid><![CDATA[${group.gid}]]></gid>
                <sid><![CDATA[544188]]></sid>
                <group_name><![CDATA[${group.name}]]></group_name>
                <group_order><![CDATA[${group.order}]]></group_order>
                <description><![CDATA[${group.description}]]></description>
                <language><![CDATA[fr]]></language>
                <randomization_group/>
                <grelevance/>
            </row>
        %endfor
        </rows>
    </groups>