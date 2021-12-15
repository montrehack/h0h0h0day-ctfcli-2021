<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/functions" prefix="fn"%>

<html>
    <head>
        <%@include file="head.jsp" %>
    </head>
    <body>
        <%@include file="nav.jsp" %>

        <c:choose>
            <c:when test="${not empty param.address}">
                <div class="alert alert-primary m-4">
                    <c:out value="We've logged your order to: ${param.address}. You should receive your logs in 5-7 business days."/>
                </div>
            </c:when>
            <c:otherwise>
                <br/>
            </c:otherwise>
        </c:choose>

        <div class="container">
            <div class="row justify-content-center">
                <div class="col-2">
                    <img src="/content/beaver.jpg"/>
                </div>
            </div>
            <br/>
            <div class="row justify-content-center">
                <div class="col-3 text-center">
                    <h5>We Chop Wood</h5>
                </div>
            </div>
        </div>

        <form class="card p-4 m-4" method="POST">
            <label for="email">Address:</label>
            <input class="form-control" type="address" id="address" name="address"/>
            <br/>
            <input class="btn btn-danger" type="submit" value="Order"/>
        </form>

        <marquee class="py-4" style="position: absolute; bottom: 0">The Loggers is offering a limited time offer of 2 logs for the price of 1. Order now and we'll double your order amount free of charge.</marquee>
    </body>
</html>
