<!DOCTYPE html>
<html>
	<head>
		% include('header.tpl')
	</head>
	<body class="index">
	%for x in range(1):
		%for i in data:
			<a href="/{{i["eventDateName"]}}" class="darken">
				<img width="20%" style="float:left;" src="{{i["imageSource"]}}"></img>
			</a>
		%end
	%end
	</body>
</html>