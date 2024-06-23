{% if response != None %}
        {% for row in response %}
        {% for stuff in row %}
        {% if stuff != None%}
        <tr>
            <td>{{stuff}}</td>
        </tr>
        {% endif %}
        {% endfor %}
        {% endfor %}
        {% endif %}