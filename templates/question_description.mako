<%page args="title, options"/>
<p>${title}</p>

<table border="1" cellpadding="0" cellspacing="1">
    <tbody>
        %for option in options:
        <tr style="border-bottom: 1px solid white;">
            <td>
                ${option.description}
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