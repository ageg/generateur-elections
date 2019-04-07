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
        <%include file="group_row.mako" args="group=group"/>
    %endfor
    </rows>
</groups>