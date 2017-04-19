/*
*       FILTERS
*/

function filter_numeric(expression, number) {
    var expr = expression.replace(/\s*/g, '').replace(/,/g, '.');
    var data = parseFloat(number);

    if (expr.match(/^<\d+\.?\d*$/)) {                           // Less than.
        var num = parseFloat(expr.match(/\d+\.?\d*/));
        return data < num ? true : false;
    }
    else if (expr.match(/^>\d+\.?\d*$/)) {                      // Greater than.
        var num = parseFloat(expr.match(/\d+\.?\d*/));
        return data > num ? true : false;
    }
    else if (expr.match(/^!=\d+\.?\d*$/)) {                     // Not equal to.
        var num = parseFloat(expr.match(/\d+\.?\d*/));
        return data != num ? true : false;
    }
    else if (expr.match(/^\d+\.?\d*$/)) {                       // Equal to.
        var num = parseFloat(expr.match(/\d+\.?\d*/));
        return data == num ? true : false;
    }
    else if (expr.match(/^\d+\.?\d*-\d+\.?\d*$/)) {             // Between X and Y
        var num1 = parseFloat(expr.match(/^\d+\.?\d*/));
        var num2 = parseFloat(expr.match(/\d+\.?\d*$/));
        return (data >= num1 && data <= num2) ? true : false;
    }
    else if (expr.match(/^<=\d+\.?\d*$/)) {                     // Less or equal than.
        var num = parseFloat(expr.match(/\d+\.?\d*/));
        return data <= num ? true : false;
    }
    else if (expr.match(/^>=\d+\.?\d*$/)) {                     // Greater or equal than.
        var num = parseFloat(expr.match(/\d+\.?\d*/));
        return data >= num ? true : false;
    }

    return true;
}

function filter_string(expression, string) {
    var expr = expression.split(" ");
    var str  = string.toLowerCase();
    var eval = true;

    // There is nothing in the filter.
    if (expr.length == 0) {
        return true;
    }

    // Match string agains every term in the expression string.
    for (var i = 0; i < expr.length; i++) {
        if (str.match(expr[i].toLowerCase())) {
            eval = eval & true;
        } else {
            eval = false;
        }
    }

    return eval;
}

function filter_regex(regex, string) {
    var expr = RegExp(regex, 'i');

    return expr.test(string);
}
